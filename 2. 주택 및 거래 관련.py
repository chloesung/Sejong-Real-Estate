#!/usr/bin/env python
# coding: utf-8

# ## 2) 주택 및 거래 관련

# ### 주택 나이 데이터

# In[ ]:


# 주택 나이 나타내는 column 추가
df = pd.merge(house,res,on='대지위치',how='right')[['X','Y','사용승인일']]
df = df.dropna()
df['사용연도'] = df['사용승인일'].astype(str).str[:4]
df['사용연도'] = 2022 - df['사용연도'].astype(int)

# 그리드 별 평균 구해주기
df = plus_grid(df, geo, 'X', 'Y').groupby('id').mean()
df = pd.merge(df,geo,on='id',how='outer')
df = GeoDataFrame(df)
age = df[['id','사용연도']].fillna(0)

# 시각화
plot_grid_map(df, col = '사용연도', title = '건축 연한', k=10,
              mode = 'cont_classify',c_mode = 'FisherJenks', colors = 'Purples', percen = False)


# ### 주택 매매 데이터

# In[ ]:


from functools import reduce
col = ['id','계약년월','평당가격','geometry','입력주소']
dfs = [apt_buy[col],vil_buy[col],ops_buy[col]]
buy = reduce(lambda left, right: pd.merge(left, right, on=col, how='outer'), dfs)


# In[ ]:


# 상승장 이전 이후로 나누기
before1 = buy.loc[buy['계약년월']<201910] #상승장 이전
after1 = buy[buy['계약년월']>201909] #상승장 이후

# 그리드 당 평균 매매 가격구하기
before = DataFrame(before1.groupby(['id']).mean()['평당가격']).reset_index()
after = DataFrame(after1.groupby(['id','계약년월']).mean()['평당가격']).reset_index()
all = DataFrame(buy.groupby(['id','계약년월']).mean()['평당가격']).reset_index()

# datetime으로 바꾸기
from datetime import datetime
after['계약년월'] = pd.to_datetime(after['계약년월'], format='%Y%m')
all['계약년월'] = pd.to_datetime(all['계약년월'], format='%Y%m')


# In[ ]:


all.to_csv('grid_price.csv', encoding='utf-8')


# In[ ]:


# 추이 간단히 시각화
plt.figure(figsize=(10,5))
for i in all['id'].unique().tolist():
    d_ = all[(all["id"]==i)]
    plt.plot(d_["계약년월"], d_["평당가격"], "-", alpha=.6)
plt.grid()
plt.title('매매 가격 추이', fontproperties=nanumr)
plt.xticks(rotation=90)
plt.show()


# ### 상승장 이전 매매 가격 평균

# In[ ]:


df_before = pd.merge(before,geo,on='id',how='outer')
df_before = GeoDataFrame(df_before)

# 시각화
plot_grid_map(df_before, # 데이터: 격자 - 수치변수 이렇게 두개만 들어와 있는 GeoDataFrame 형태여야함
              col = '평당가격', # 수치변수 들어와있는 컬럼명
              title = '상승장 이전 매매가격 평균', # 시각화에 붙이고 싶은 제목 
              k =10, # 수치변수를 몇단계로 나누고 싶은지
              mode = 'cont_classify', #FisherJenks나 NaturalBreaks(KMeans) 쓸거면 얘 그냥 적으면 됨
              c_mode = 'FisherJenks', #케이민즈 쓰고 싶으면 NaturalBreaks 쓰기
              colors = 'Greens', #쓰고 싶은 색깔,, Blues Greens Purples 등등 다 가능함
              percen = False)


# ### 매매 거래 건수

# In[ ]:


df = buy.dropna()
df = df.groupby('id').count().reset_index()[['id','평당가격']]
df = pd.merge(df,geo,on='id',how='outer')
df = GeoDataFrame(df)

# 시각화
plot_grid_map(df, col = '평당가격', title = '매매 거래 건수', k=10,
              mode = 'cont_classify',c_mode = 'FisherJenks', colors = 'Blues', percen = False)


# In[ ]:


df = before1.dropna()
df = df.groupby('id').count().reset_index()[['id','평당가격']]
df = pd.merge(df,geo,on='id',how='outer')
df = GeoDataFrame(df)

# 시각화
plot_grid_map(df, col = '평당가격', title = '상승장 이전 매매 거래 건수', k=10,
              mode = 'cont_classify',c_mode = 'FisherJenks', colors = 'Blues', percen = False)


# In[ ]:


df = after1.dropna()
df = df.groupby('id').count().reset_index()[['id','평당가격']]
df = pd.merge(df,geo,on='id',how='outer')
df = GeoDataFrame(df)

# 시각화
plot_grid_map(df, col = '평당가격', title = '상승장 이후 매매 거래 건수', k=10,
              mode = 'cont_classify',c_mode = 'FisherJenks', colors = 'Blues', percen = False)


# ### 매매 실거래가 추이 Clustering

# In[ ]:


#그리드 당 매매가격 불러오기
grid_price = all.copy()

#계약년월 열에 날짜 속성 부여 
grid_price_n = grid_price.set_index('계약년월')

#1년 단위로 자료 resampling
grid_price_y = grid_price_n.groupby('id')['평당가격'].resample('Y').mean().reset_index()
grid_price_y['year'] = grid_price_y['계약년월'].dt.year

df1 = grid_price_y.pivot(index='id', columns='year', values='평당가격').reset_index()

#결측치 3개 이상인 값 drop
df1.dropna(thresh=3, inplace=True)

#결측치 0으로 대체
df1.fillna(0, inplace=True)
value = df1.iloc[:,1:]


# In[ ]:


#AgglomerativeClustering을 이용하여, 7개의 군집으로 clustering
cluster_price = AgglomerativeClustering(n_clusters=7, affinity='euclidean', linkage='ward')
cluster_price.fit_predict(value)
df1["cluster"] = cluster_price.fit_predict(value)
df2 = pd.melt(df1, id_vars=['id'], value_vars=df1.iloc[:,1:-1], value_name='평당가격')
df3 = df1[['id', 'cluster']]
df4 = pd.merge(df2, df3, on = 'id', how = 'left')

#연도만 따로 추출한 year 열에 날짜 속성 부여
df4['year'] = pd.to_datetime(df4['year'], format='%Y')


# In[ ]:


#군집 순서를 완만->급격 순으로 임의 조정
df4['cluster_n'] = df4['cluster'] + 10
df4['cluster_n'].replace(to_replace=[10,11,12,13,14,15,16], value= [0,2,6,3,1,5,4], inplace=True)
df4 = df4.drop(['cluster'], axis=1)
df4.rename(columns = {'cluster_n':'cluster'}, inplace=True)

#군집 순서를 완만->급격 순으로 임의 조정
df_price = df1[['id', 'cluster']]
df_price['cluster_n'] = df_price['cluster'] + 10
df_price['cluster_n'].replace(to_replace=[10,11,12,13,14,15,16], value= [0,2,6,3,1,5,4], inplace=True)
df_price = df_price.drop(['cluster'], axis=1)
df_price.rename(columns = {'cluster_n':'cluster'}, inplace=True)


# ### 클러스터 별 plot

# In[ ]:


#군집1 plot
cluster_1 = df4[df4['cluster'] == 0]

plt.figure(figsize=(10,5))
for i in cluster_1['id'].unique().tolist():
    d_ = cluster_1[(cluster_1["id"]==i)]
    plt.plot(d_["year"], d_["평당가격"], "-", alpha=.6)
plt.grid()
plt.title('군집1_매매가격 추이', fontproperties=nanumr)
plt.xticks(rotation=90)
plt.show()


# In[ ]:


#군집2 plot
cluster_2 = df4[df4['cluster'] == 1]

plt.figure(figsize=(10,5))
for i in cluster_2['id'].unique().tolist():
    d_ = cluster_2[(cluster_2["id"]==i)]
    plt.plot(d_["year"], d_["평당가격"], "-", alpha=.6)
plt.grid()
plt.title('군집2_매매가격 추이', fontproperties=nanumr)
plt.xticks(rotation=90)
plt.show()


# In[ ]:


#군집3 plot
cluster_3 = df4[df4['cluster'] == 2]

plt.figure(figsize=(10,5))
for i in cluster_3['id'].unique().tolist():
    d_ = cluster_3[(cluster_3["id"]==i)]
    plt.plot(d_["year"], d_["평당가격"], "-", alpha=.6)
plt.grid()
plt.title('군집3_매매가격 추이', fontproperties=nanumr)
plt.xticks(rotation=90)
plt.show()


# In[ ]:


#군집4 plot
cluster_4 = df4[df4['cluster'] == 3]

plt.figure(figsize=(10,5))
for i in cluster_4['id'].unique().tolist():
    d_ = cluster_4[(cluster_4["id"]==i)]
    plt.plot(d_["year"], d_["평당가격"], "-", alpha=.6)
plt.grid()
plt.title('군집4_매매가격 추이', fontproperties=nanumr)
plt.xticks(rotation=90)
plt.show()


# In[ ]:


#군집5 plot
cluster_5 = df4[df4['cluster'] == 4]

plt.figure(figsize=(10,5))
for i in cluster_5['id'].unique().tolist():
    d_ = cluster_5[(cluster_5["id"]==i)]
    plt.plot(d_["year"], d_["평당가격"], "-", alpha=.6)
plt.grid()
plt.title('군집5_매매가격 추이', fontproperties=nanumr)
plt.xticks(rotation=90)
plt.show()


# In[ ]:


#군집6 plot
cluster_6 = df4[df4['cluster'] == 5]

plt.figure(figsize=(10,5))
for i in cluster_6['id'].unique().tolist():
    d_ = cluster_6[(cluster_6["id"]==i)]
    plt.plot(d_["year"], d_["평당가격"], "-", alpha=.6)
plt.grid()
plt.title('군집6_매매가격 추이', fontproperties=nanumr)
plt.xticks(rotation=90)
plt.show()


# In[ ]:


#군집7 plot
cluster_7 = df4[df4['cluster'] == 6]

plt.figure(figsize=(10,5))
for i in cluster_7['id'].unique().tolist():
    d_ = cluster_7[(cluster_7["id"]==i)]
    plt.plot(d_["year"], d_["평당가격"], "-", alpha=.6)
plt.grid()
plt.title('군집7_매매가격 추이', fontproperties=nanumr)
plt.xticks(rotation=90)
plt.show()


# In[ ]:


#격자 데이터와 병합
price_merge = pd.merge(df_price, geo, on = 'id', how = 'right')

#cluster 순서에 따라 데이터 정렬
price_merge.sort_values('cluster', inplace=True)

#geodataframe으로 변환
price_merge = gpd.GeoDataFrame(price_merge)


# In[ ]:


# 시각화
plot_grid_map(price_merge, col = 'cluster', title = '평당가격 클러스터링', mode = 'cluster',
              c_mode = 'NaturalBreaks', colors = 'Blues', percen = False)


# ### 주택 전세 데이터

# In[ ]:


from functools import reduce
col = ['id','계약년월','평당가격','geometry','입력주소']
dfs = [apt_full[col],vil_full[col],ops_full[col]]
full = reduce(lambda left, right: pd.merge(left, right, on=col, how='outer'), dfs)


# In[ ]:


# 그리드 당 평균 전세 가격구하기
df = DataFrame(full.groupby(['id','계약년월']).mean()['평당가격']).reset_index()

# datetime으로 바꾸기
from datetime import datetime
df['계약년월'] = pd.to_datetime(df['계약년월'], format='%Y%m')

# 추이 간단히 시각화
plt.figure(figsize=(10,5))
for i in df['id'].unique().tolist():
    d_ = df[(df["id"]==i)]
    plt.plot(d_["계약년월"], d_["평당가격"], "-", alpha=.6)
plt.grid()
plt.title('전세 가격 추이', fontproperties=nanumr)
plt.xticks(rotation=90)
plt.show()


# ### 주택 임대 데이터

# In[ ]:


from functools import reduce
col = ['id','계약년월', 'geometry','입력주소']
dfs = [apt_rent[col],vil_rent[col],ops_rent[col]]
rent = reduce(lambda left, right: pd.merge(left, right, on=col, how='outer'), dfs)
before2 = rent[rent['계약년월']<201910] #상승장 이전
after2 = rent[rent['계약년월']>201909] #상승장 이후


# In[ ]:


# 그리드 당 평균 임대 건수구하기
df = DataFrame(rent.groupby(['id','계약년월']).count()['입력주소']).reset_index()

# datetime으로 바꾸기
from datetime import datetime
df['계약년월'] = pd.to_datetime(df['계약년월'], format='%Y%m')

# 추이 간단히 시각화
plt.figure(figsize=(10,5))
for i in df['id'].unique().tolist():
    d_ = df[(df["id"]==i)]
    plt.plot(d_["계약년월"], d_["입력주소"], "-", alpha=.6)
plt.grid()
plt.legend(fontsize=13)
plt.xticks(rotation=90)
plt.show()


# ### 임대 거래 건수

# In[ ]:


df = rent.dropna()
df = df.groupby('id').count().reset_index()[['id','입력주소']]
df = pd.merge(df,geo,on='id',how='outer')
df = GeoDataFrame(df)

# 시각화
plot_grid_map(df, col = '입력주소', title = '임대 거래 건수', mode = 'cont_classify', k=10,
              c_mode = 'FisherJenks', colors = 'Blues', percen = False)


# In[ ]:


df = before2.dropna()
df = df.groupby('id').count().reset_index()[['id','입력주소']]
df = pd.merge(df,geo,on='id',how='outer')
df = GeoDataFrame(df)

# 시각화
plot_grid_map(df, col = '입력주소', title = '상승장 이전 임대 거래 건수', mode = 'cont_classify', k=10,
              c_mode = 'FisherJenks', colors = 'Blues', percen = False)


# In[ ]:


df = after2.dropna()
df = df.groupby('id').count().reset_index()[['id','입력주소']]
df = pd.merge(df,geo,on='id',how='outer')
df = GeoDataFrame(df)

# 시각화
plot_grid_map(df, col = '입력주소', title = '상승장 이후 임대 거래 건수', mode = 'cont_classify', k=10,
              c_mode = 'FisherJenks', colors = 'Blues', percen = False)


# ### 행정동별 전세가율 추이

# In[ ]:


# 아파트 데이터만 불러오기
aptb = apt_buy.dropna()
aptf = apt_full.dropna()
aptb['시군구'] = aptb['시군구'].str[8:11]
aptf['시군구'] = aptf['시군구'].str[8:11]

# 날짜 별로 정렬
aptf = DataFrame(aptf.groupby(['시군구','입력주소','계약년월']).mean()['평당가격']).reset_index()
aptb = DataFrame(aptb.groupby(['시군구','입력주소','계약년월']).mean()['평당가격']).reset_index()

df2 = pd.merge(aptb, aptf, on=['시군구','입력주소', '계약년월'], how='outer')
df2['전세가율'] = 100*df2['평당가격_y']/df2['평당가격_x']
df2['계약년월'] = pd.to_datetime(df2['계약년월'], format='%Y%m')

df2 = df2.dropna().groupby(['시군구', '계약년월']).mean().unstack()['전세가율'].transpose()

# 시각화
fig = make_subplots(rows=1, cols=1, shared_xaxes=True)
for i in df2.columns.tolist():
    fig.add_trace(go.Scatter(x=df2.index,y=df2[i],
             mode='lines', name=i))
fig.update_layout(title='세종시 전세가율 추이', plot_bgcolor='#F8F7F1')
fig.show()


# In[ ]:


# Data Merging
df2 = DataFrame(df2.mean()).reset_index()
df2 = df2.replace('조치원','조치원읍')
df2 = pd.merge(df2,data31,left_on='시군구',right_on='EMD_KOR_NM',how='outer')
df2 = GeoDataFrame(df2)

# 시각화
plot_grid_map(df2, col = 0, title = '전세가율',mode = 'cont_classify', k=10,
              c_mode = 'FisherJenks', colors = 'Blues', percen = True)


# ### 공시지가 변동률

# In[ ]:


# 연도별 공시지가 변동률 구하기

df = gongsi.groupby(['지번주소','id','기준년도']).mean()['공시지가'].unstack()
df = df.dropna(thresh=2)
df = df.reset_index()

# 변동률이기에 로그 근사 시켜주기

df['17-18'] = (df[2018.0] - df[2017.0])/df[2017.0] +1
df['18-19'] = (df[2019.0] - df[2018.0])/df[2018.0] +1
df['19-20'] = (df[2020.0] - df[2019.0])/df[2019.0] +1

df[['17-18','18-19','19-20']] = np.log(df[['17-18','18-19','19-20']])
df[[2017.0, 2018.0, 2019.0, 2020.0]] = df[[2017.0, 2018.0, 2019.0, 2020.0]]*3.3/10000
df.fillna(0)
df['변동률'] = (df['17-18'] + df['18-19'] + df['19-20'])*100/3
gongsi2 = df.groupby('id').mean().reset_index()


# In[ ]:


gongsi2 = pd.merge(gongsi2,geo,on='id',how='outer')
df2 = GeoDataFrame(gongsi2)

# 시각화
plot_grid_map(df2, col = '변동률', title = '공시지가 변동률',mode = 'cont_classify', k=10,
              c_mode = 'FisherJenks', colors = 'BuGn', percen = True)


# ### 2020년 공시지가

# In[ ]:


# 시각화
plot_grid_map(df2, col = 2020.0, title = '2020년 공시지가',mode = 'cont_classify', k=10,
              c_mode = 'FisherJenks', colors = 'BuGn', percen = False)

