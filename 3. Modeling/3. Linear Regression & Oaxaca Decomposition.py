#!/usr/bin/env python
# coding: utf-8

# ## 3) Multiple Regression Analysis
# 
# - 두 개 이상의 연속형 독립변수가 연속형 종속변수에는 미치는 영향을 검증하는 분석 방법
# 
# - 독립변수 분석: 종속변수와 관련이 있는 주요 독립변수 파악

# ### 격자 Data  전처리

# In[ ]:


# 격자데이터 읍면동별로 분류
df = gpd.sjoin(geo, data32, op='intersects', how='left')
dff = df.groupby('id').count().reset_index()
fine = dff[dff['left'] == 1][['id','left']]#하나씩으로 정상적으로 나눠진 데이터
fine = pd.merge(fine, df, on='id')[['id','ADM_DR_NM','left_x']]
dff = dff[dff['left']>1][['id','left']] #두개 이상이 할당된 데이터
df2 = pd.merge(dff, df, on='id')[['id','ADM_DR_NM','left_x']]

# 조치원 부분만 처리
eup = df2[df2['ADM_DR_NM'].str[3] == '읍']
a = eup['id'].unique().tolist()
eup = df2[df2['id'].isin(a)]
df2 = df2.drop(eup.index)
eup = eup[eup['ADM_DR_NM'].str[3] == '읍']


# 중복되는 읍면동 drop
dropdu = df2[['id','left_x']].drop_duplicates().index
df2 = df2.loc[dropdu,:]
done = pd.concat([fine, df2, eup])
emdgeo = pd.merge(done,geo, on='id')


# In[ ]:


# 읍면동 지역으로 나누어서 그리드 확인
eup = emdgeo[emdgeo['ADM_DR_NM'].str[3] == '읍']
myun = emdgeo[emdgeo['ADM_DR_NM'].str[2] == '면']
dong = emdgeo[emdgeo['ADM_DR_NM'].str[2] == '동']

print('읍: ', len(eup))
print('면: ', len(myun))
print('동: ', len(dong))


# In[ ]:


# 지역구분 column 추가
eup['지역 구분'] = '읍'
myun['지역 구분'] = '면'
dong['지역 구분'] = '동'
df = pd.concat([eup, myun, dong])


# ### 지수(생활 편의, 안전, 교통), 공시지가, 인구 데이터 Column으로 추가

# In[ ]:


life_rate.columns = ['life','id']
safety_rate.columns = ['safety','id']
transport_rate.columns = ['transport','id']
gs = gongsi2[['id',2020,'변동률']]
gs.columns = ['id','공시지가','공시지가 변동률']
pop2020 = pop2020[['id','총합']].fillna(0).replace(0,1)


# In[ ]:


popin = popin[['index',0]].fillna(0)
popin.columns = ['ADM_DR_NM','순전입자수']
# 순전입자수가 너무 많기 때문에 scaling 진행
min_max_scaler = MinMaxScaler(feature_range=(5,100))
x=popin['순전입자수']
x=x.to_numpy(dtype=float)
x=x.reshape(-1,1)
x1= min_max_scaler.fit_transform(x)
popin['순전입자수'] = x1


# In[ ]:


age = age.replace(0,1)


# In[ ]:


from functools import reduce
dfs = [df,life_rate,safety_rate,transport_rate, gs, age, pop2020]
df_merge = reduce(lambda left, right: pd.merge(left, right, on='id', how='outer'), dfs, )
df_merge = pd.merge(df_merge, popin, on='ADM_DR_NM')
emd = df_merge.drop(['left_x','left','top','bottom','SIG_CD','SIG_KOR_NM'],axis=1)


# In[ ]:


eup = emd[emd['지역 구분'] == '읍']
myun = emd[emd['지역 구분'] == '면']
dong = emd[emd['지역 구분'] == '동']


# ### 다중선형회귀( Level-log Model) 함수 정의
# 
# - x가 1%만큼 증가할 때 y가 $\frac{\beta}{100}$% 만큼 변하는 것을 의미하는 분석 방법 ➡︎ 독립변수를 단위화  
#   
# - 독립변수가 단위에 영향을 받지 않도록 행복지수, 안전지수, 교통지수에 대해서 Level-log Model을 사용

# In[ ]:


from statsmodels.formula.api import ols

def log(df):
    # 공시지가 na 값 drop 후, na 아닌 데이터만 추출
    df=df.reset_index()
    df1=df['공시지가'].dropna()
    index=df1.index
    df=df.loc[index]
    df = df.fillna(0)

    # 로그 씌워주기
    df['log생활지수']=np.log(df['life'])
    df['log안전지수']=np.log(df['safety'])
    df['log교통지수']=np.log(df['transport'])
    df['log건축연한']=np.log(df['사용연도'])
    df['건축연한']=df['사용연도']
    df['log순전입자수']=np.log(df['순전입자수'])

    return df

def ourols(df, log=False):
    # 회귀 돌려주기
    res = ols('공시지가 ~ log생활지수+log안전지수+log교통지수+순전입자수', data=df).fit()
        
    return res


# ### 읍 (log-level)

# In[ ]:


res1 = ourols(log(eup))
res1.summary()


# ### 면 (log-level)

# In[ ]:


res2 = ourols(log(myun))
res2.summary()


# ### 동 (log-level)

# In[ ]:


res3 = ourols(log(dong))
res3.summary()


# ## 4) Oaxaca-Blinder Decomposition

# - 선형회귀계수를 이용해 격차를 세 가지 부분으로 분해해 격차의 발생요인을 설명하는 분석 방법
# 
# - 가격 격차가 어디서 기인하는지 분석하기 위해 Oaxaca-Blinder 분해법 적용

# ### Preprocessing

# In[ ]:


# 읍 X와 y값 지정.
X_eup=log(eup)[['log생활지수','log안전지수','log교통지수','순전입자수']]
y_eup=log(eup)['공시지가']

# 면 X와 y값 지정.
X_myun=log(myun)[['log생활지수','log안전지수','log교통지수','순전입자수']]
y_myun=log(myun)['공시지가']

# 동 X와 y값 지정.
X_dong=log(dong)[['log생활지수','log안전지수','log교통지수','순전입자수']]
y_dong=log(dong)['공시지가']


# In[ ]:


# 읍, 면 vs 동 Beta(coefficient)계수 벡터화
b_eup = np.asarray(res1.params[1:])
b_myun = np.asarray(res2.params[1:])
b_dong = np.asarray(res3.params[1:])


# In[ ]:


# 읍, 면 vs 동 독립변수 mean 벡터화
x_eup = np.asarray(X_eup.mean())
x_myun = np.asarray(X_myun.mean())
x_dong = np.asarray(X_dong.mean())


# In[ ]:


print('읍 공시지가 평균: ',y_eup.mean())
print('면 공시지가 평균: ',y_myun.mean())
print('동 공시지가 평균: ',y_dong.mean())


# ### Modeling

# - Endowments: 설명 변수 차이로 인해 발생하는 격차
# 
# - Coefficients: 각 그룹의 회귀 계수 차이로 인해 발생하는 격차
# 
# - Interaction: 모델로 설명할 수 없는 부분 (잔차)

# In[ ]:


def oaxaca(x1, x2, b1, b2):
    
    X=x1-x2
    B=b1-b2
    
    endowments=[]
    coefficients=[]
    interaction=[]
    
    for i in range(4):
        endowments.append(X[i]*b2[i])
        coefficients.append(x2[i]*B[i])
        interaction.append(X[i]*B[i])
    df = DataFrame()
    df['endowments'] = endowments
    df['coefficents'] = coefficients
    df['interaction'] = interaction
    df['variable'] = ['loglife','logsafety','logtransport','순전입자수']
    df = df.set_index('variable')
    df2 = DataFrame(df.transpose())
    df2['sum'] = df.sum()
    return df2


# In[ ]:


oaxaca(x_dong, x_myun, b_dong, b_myun)


# In[ ]:


oaxaca(x_dong, x_eup, b_dong, b_eup)

