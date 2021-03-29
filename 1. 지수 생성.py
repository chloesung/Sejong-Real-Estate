#!/usr/bin/env python
# coding: utf-8

# - - -
# # 3. Modeling

# ## 1) 지수 생성

# ## Clustering

# ### 클러스터링 함수 정의

# In[ ]:


# pydeck 용 coordinates 만들어주기
def multipolygon_to_coordinates(x):
    lon, lat = x[0].exterior.xy
    return [[x, y] for x, y in zip(lon, lat)]

data32['coordinates'] = data32['geometry'].apply(multipolygon_to_coordinates)


# In[ ]:


# 시각화 함수
def clustermap(df, X, Y):
    layer1 = pdk.Layer('ScatterplotLayer', # 사용할 Layer 타입
                  df, # 시각화에 쓰일 데이터프레임
                  get_position=[X, Y], # geometry 정보를 담고있는 컬럼 이름
                  get_color='색상', # 각 데이터 별 rgb 또는 rgba 값 (0~255) # 마지막이 투명도 (0~255사이)
                  get_radius=100
                  #wireframe=True, # 마우스 오버(hover) 시 박스 출력 
                  ) # 3D의 경우 값의 높이를 val 변수를 통해 하겠다.

    layer2 = pdk.Layer('PolygonLayer', 
                       data32, 
                       get_polygon='coordinates', 
                       get_fill_color='[100,150,200,30]',
                       get_line_color='[255, 255, 255]',
                       pickable=True, 
                       lineWidthScale=15,
                       auto_highlight=True)

    center = [127.261575, 36.562811]
    view_state = pdk.ViewState(
        longitude=center[0],
        latitude=center[1],
        zoom=9.7)

    r = pdk.Deck(layers=[layer1,layer2], initial_view_state=view_state,
                 mapbox_key ='pk.eyJ1Ijoia3Nra253IiwiYSI6ImNra2NyejlqNzAzamsyb3BtbndvMnVvZjYifQ.xGhIzKCQe1mfade6s__fNw', 
                 map_style='mapbox://styles/mapbox/dark-v9')

    return r


# ### 상권 클러스터링

# In[ ]:


# HDBSCAN으로 상권 클러스터링
clusterer = hdbscan.HDBSCAN(cluster_selection_epsilon=0.0022)
df = data14
clusterer.fit(df[['lon', 'lat']])
df['cluster'] = clusterer.labels_
print(len(df['cluster'].unique()))
print(len(df[df['cluster'] == -1]))
df = df[df['cluster'] != -1]


# In[ ]:


색상 = []
for kind in df['cluster']:
    np.random.seed(kind + 10000)
    
    색상_temp = np.random.randint(250, size=(3, )).tolist()
    if kind == -1:
        색상_temp.extend([0])
    else:
        색상_temp.extend([170])
    
    색상.append(색상_temp)
    
df['색상'] = 색상
df = df.reset_index(drop=True)


# In[ ]:


clustermap(df, 'lon','lat').to_html()


# In[ ]:


drop = df.groupby('cluster').count()['lon'][df.groupby('cluster').count()['lon'] <= 25].index
clustermap(df[~df['cluster'].isin(drop)], 'lon','lat').to_html()


# In[ ]:


print('제거 전: ', len(df['cluster'].unique()))
print('제거 후: ', len(df[~df['cluster'].isin(drop)]['cluster'].unique()))


# In[ ]:


store_delete = df[~df['cluster'].isin(drop)]
store_delete = gpd.GeoDataFrame(store_delete, geometry= gpd.points_from_xy(store_delete.lon, store_delete.lat))


# In[ ]:


#같은 군집에 속하는 좌표들의 합집합을 구하고, 그 합집합의 중점 구하기
aca_cluster = {"cluster":[],"lon":[], "lat":[]}

for i in list(store_delete.cluster.unique()):
    aca_cluster["cluster"].append(i)
    aca_cluster["lon"].append(store_delete[store_delete.cluster == i].unary_union.centroid.x)
    aca_cluster["lat"].append(store_delete[store_delete.cluster == i].unary_union.centroid.y)
    
store_cluster_df = pd.DataFrame(aca_cluster)
store_cluster_geo = gpd.GeoDataFrame(store_cluster_df, geometry = gpd.points_from_xy(store_cluster_df.lon,store_cluster_df.lat))
store_cluster_geo.crs = geo.crs


# ### 학원가 클러스터링

# In[ ]:


# HDBSCAN으로 학원가 클러스터링
clusterer = hdbscan.HDBSCAN(cluster_selection_epsilon=0.003)
df = academy 
clusterer.fit(df[['X', 'Y']])
df['cluster'] = clusterer.labels_
print(len(df['cluster'].unique()))
print(len(df[df['cluster'] == -1]))
df = df[df['cluster'] != -1]


# In[ ]:


색상 = []
for kind in df['cluster']:
    np.random.seed(kind + 10000)
    
    색상_temp = np.random.randint(250, size=(3, )).tolist()
    if kind == -1:
        색상_temp.extend([0])
    else:
        색상_temp.extend([170])
    
    색상.append(색상_temp)
    
df['색상'] = 색상
df = df.reset_index(drop=True)


# In[ ]:


clustermap(df, 'X','Y').to_html()


# In[ ]:


drop = df.groupby('cluster').count()['X'][df.groupby('cluster').count()['X'] <= 20].index
clustermap(df[~df['cluster'].isin(drop)], 'X','Y').to_html()


# In[ ]:


print('제거 전: ', len(df['cluster'].unique()))
print('제거 후: ', len(df[~df['cluster'].isin(drop)]['cluster'].unique()))


# In[ ]:


academy_delete = df[~df['cluster'].isin(drop)]
academy_delete = gpd.GeoDataFrame(academy_delete, geometry= gpd.points_from_xy(academy_delete.X, academy_delete.Y))


# In[ ]:


#같은 군집에 속하는 좌표들의 합집합을 구하고, 그 합집합의 중점 구하기
aca_cluster = {"cluster":[],"lon":[], "lat":[]}

for i in list(academy_delete.cluster.unique()):
    aca_cluster["cluster"].append(i)
    aca_cluster["lon"].append(academy_delete[academy_delete.cluster == i].unary_union.centroid.x)
    aca_cluster["lat"].append(academy_delete[academy_delete.cluster == i].unary_union.centroid.y)
    
academy_cluster_df = pd.DataFrame(aca_cluster)
academy_cluster_geo = gpd.GeoDataFrame(academy_cluster_df, geometry = gpd.points_from_xy(academy_cluster_df.lon,academy_cluster_df.lat))
academy_cluster_geo.crs = geo.crs


# ## 지수 생성용 전처리

# In[ ]:


# 그리드 별 개수 구해서 추가하는 함수 정의
def grid_count(df, name):
    df = df.groupby('id').count().reset_index()
    df = df[['id','SIG_KOR_NM']]
    df.columns = ['id', name]
    return df

# 그리드 별 평균 구해서 추가하는 함수 정의
def grid_mean(df, name):
    df = df.groupby('id').mean().reset_index()
    df = df[['id','SIG_KOR_NM']]
    df.columns = ['id', name]
    return df


# ### 안전 지수

# In[ ]:


# 그리드 별 가로등 개수 구하기
df_light = grid_count(street_lights, '가로등')

# 그리드 별 파출소 개수 구하기
df_police_office = grid_count(police_office, '파출소')

# 그리드 별 cctv 개수 구하기
df_cctv = cctv.groupby('id').sum().reset_index()[['id','카메라대수']]
df_cctv['카메라대수'] = df_cctv['카메라대수']*9


# In[ ]:


from functools import reduce
dfs = [geo, df_light, df_police_office, df_cctv]
df_merge = reduce(lambda left, right: pd.merge(left, right, on='id', how='outer'), dfs)
df_merge = df_merge.drop(['left','top','right','bottom','SIG_CD','SIG_KOR_NM'],axis=1)
safety = df_merge


# ### 교통 지수

# 역, 터미널과의 거리의 경우에는,  
# - 오송역  
# - 반석역  
# - 조치원역  
# - 세종고속시외버스터미널  
# - 조치원공영버스터미널   
# 을 고려함
# 
# 제외한 역  
# - 전의역, 부강역도 하루에 몇 번 정차하지만 이용하기 불편한 횟수  
# - 전동역, 서창역, 내판역, 매포역, 소정리역은 모든 여객열차가 정차하지 않음  
# - 청주역: 충북이기도 하고, 사람들이 엄청 다니는 역도 아님.  

# In[ ]:


# 그리드 별 버스 별 배차 개수 구하기
df_bus = bus[['id','BRT','광역버스','지선버스','간선버스','마을버스']]
df_bus=df_bus.groupby(["id"])['BRT','광역버스','지선버스','간선버스','마을버스'].sum().reset_index()

#  그리드 별 중앙 좌표와 가까운 역, 터미널과의 거리 구하기
station = pd.read_csv('sejong_stations.csv')
station_geo= gpd.GeoDataFrame(station, geometry = gpd.points_from_xy(station.경도, station.위도))
station_geo.crs = geo.crs

distance_station = []

for i in geo['geometry']:
    temp = []
    for j in station_geo['geometry']:
        temp.append(i.distance(j))
    
    distance_station.append(min(temp)) 
    
station_dist = geo.copy()
station_dist["역 터미널"] = distance_station
station_dist = station_dist[['id', '역 터미널']]


# In[ ]:


from functools import reduce
dfs = [geo, df_bus, station_dist]
df_merge = reduce(lambda left, right: pd.merge(left, right, on='id', how='outer'), dfs)
df_merge = df_merge.drop(['left','top','right','bottom','SIG_CD','SIG_KOR_NM'],axis=1)


# In[ ]:


# 거리가 멀수록 페널티를 주기 위해 Hyperbolic Tangent 도함수에 넣어준 뒤, 정규화를 진행합니다
def diff_tanh(x):
    return 4/(np.exp(2*x)+2+np.exp(-2*x))

dfdf = diff_tanh(df_merge['역 터미널'])

dfdf = pd.DataFrame(dfdf, columns=['역 터미널'])
df_merge['역 터미널']=dfdf['역 터미널']
transport=df_merge


# ### 생활 편의 지수

# In[ ]:


# 그리드 별 병원 개수 구하기
df_hospital = grid_count(hospital, '병원')

# 그리드 별 은행 개수 구하기
df_banks = grid_count(banks, '은행')

# 그리드 별 학교 개수 구하기
df_schools = school.groupby(['id','학교구분']).count().unstack()
df_schools = df_schools[df_schools.columns[0:3]].reset_index()
df_schools.columns = ['id','고등학교', '중학교', '초등학교']

# 그리드 별 공원 개수 구하기
df_parks = grid_count(parks, '공원')

# 그리드 별 학원 개수 구하기
df_academy = grid_count(academy, '학원')

# 그리드 별 편의점 개수 구하기
df_stores = grid_count(stores, '편의점')

# 그리드 별 마트 개수 구하기
df_mart = grid_count(mart, '마트')

# 그리드 별 약국 개수 구하기
df_pharmacy = grid_count(pharmacy, '약국')

# 그리드 별 중앙 좌표와 가까운 상권과의 거리 구하기
distance_store = []
for i in geo['geometry']:
    temp = []
    for j in store_cluster_geo['geometry']:
        temp.append(i.distance(j))
    
    distance_store.append(min(temp))
store_dist = geo.copy()
store_dist["상권"] = distance_store
store_dist = store_dist[['id', '상권']]


# 그리드 별 중앙 좌표와 가까운 학원가와의 거리 구하기
distance_academy = []
for i in geo['geometry']:
    temp = []
    for j in academy_cluster_geo['geometry']:
        temp.append(i.distance(j))
    
    distance_academy.append(min(temp)) 
academy_dist = geo.copy()
academy_dist["학원가"] = distance_academy
academy_dist = academy_dist[['id', '학원가']]


# In[ ]:


from functools import reduce
dfs = [geo, df_hospital, df_banks, df_schools, df_parks, df_academy, 
       df_stores, df_pharmacy, df_mart, store_dist, academy_dist]
df_merge = reduce(lambda left, right: pd.merge(left, right, on='id', how='outer'), dfs)
df_merge = df_merge.drop(['left','top','right','bottom','SIG_CD','SIG_KOR_NM'],axis=1)


# In[ ]:


# 거리가 멀수록 페널티를 주기 위해 Hyperbolic Tangent 도함수에 넣어준 뒤, 정규화를 진행합니다
def diff_tanh(x):
    return 4/(np.exp(2*x)+2+np.exp(-2*x))

dfdf = diff_tanh(df_merge[['상권','학원가']])
df_merge[['상권','학원가']]=dfdf[['상권','학원가']]
life = df_merge


# ## PCA

# - 여러 변수 간 존재하는 상관관계를 이용, 이를 대표하는 주성분을 추출하여 차원 축소하는 방법
# 
# - 각각 요소의 특징을 가장 잘 대변하는 단일 종합 지수 생성을 위해 PCA 선택

# ### 생활지수 
# 
# - 은행, 초등학교, 중학교, 고등학교, 공원, 학원, 편의점, 약국, 마트, 병원, 그리드별 가까운 상권/학원가와의 직선거리

# In[ ]:


# NA 값은 0개이기에, 0으로 입력해준다.
life['은행']=life['은행'].fillna(0)
life['고등학교']=life['고등학교'].fillna(0)
life['중학교']=life['중학교'].fillna(0)
life['초등학교']=life['초등학교'].fillna(0) 
life['공원']=life['공원'].fillna(0)
life['학원']=life['학원'].fillna(0)
life['편의점']=life['편의점'].fillna(0) 
life['약국']=life['약국'].fillna(0)
life['마트']=life['마트'].fillna(0)
life['병원']=life['병원'].fillna(0)


# In[ ]:


# PCA 후, plot_grid_map을 하기 위해 ID가 필요하므로 미리 추출한다.
id=life['id']

# PCA를 위해 x 설정.
x=life[['은행','고등학교','중학교','초등학교','공원','학원','편의점','약국','마트','상권','학원가']]

# PCA를 활용하여 지수를 만드는 것이기에, n_components 1로 고정.

pca= PCA(n_components = 1)
PC=pca.fit_transform(x)
result1 = pd.DataFrame(PC, columns=['PC1'])
result1['id']=id # pca결과에 id 데이터 추가.

# PCA PC1값에 minmax scaling을 해주었다. 
# 이유: 다중회귀분석 
min_max_scaler = MinMaxScaler(feature_range=(5,100))
x=result1['PC1']
x=x.to_numpy(dtype=float)
x=x.reshape(-1,1)
x1= min_max_scaler.fit_transform(x)
result1 = pd.DataFrame(x1, columns=['PC1'])
result1['id']=id # pca결과에 id 데이터 추가.
life_rate = result1


# ### 안전지수
# 
# - 가로등, 파출소, CCTV 대수

# In[ ]:


# NA 값은 0개이기에, 0으로 채워준다.
safety['가로등']=safety['가로등'].fillna(0)
safety['파출소']=safety['파출소'].fillna(0)
safety['카메라대수']=safety['카메라대수'].fillna(0)


# In[ ]:


# PCA 후, plot_grid_map을 하기 위해 ID가 필요하므로 미리 추출한다.
id=safety['id']
x=safety[['가로등','파출소','카메라대수']]

# PCA를 활용하여 지수를 만드는 것이기에, n_components 1로 고정.
pca= PCA(n_components = 1)
PC=pca.fit_transform(x)
result2 = pd.DataFrame(PC, columns=['PC1'])
result2['id']=id

# PCA PC1값에 minmax scaling을 해주었다. 
# 이유: 다중회귀분석 
x=result2['PC1']
x=x.to_numpy(dtype=float)
x=x.reshape(-1,1)
x1= min_max_scaler.fit_transform(x)
result2 = pd.DataFrame(x1, columns=['PC1'])
result2['id']=id 
safety_rate = result2


# ### 교통지수
# 
# - BRT, 광역, 지선, 간선, 마을버스 기준 그리드별 배차 횟수, 그리드별 중앙 좌표와 가까운 역, 터미널과의 거리

# In[ ]:


transport['BRT']=transport['BRT'].fillna(0) # NA값 0으로 대체
transport['광역버스']=transport['광역버스'].fillna(0)
transport['지선버스']=transport['지선버스'].fillna(0)
transport['간선버스']=transport['간선버스'].fillna(0)
transport['마을버스']=transport['마을버스'].fillna(0)


# In[ ]:


# PCA 후, plot_grid_map을 하기 위해 ID가 필요하므로 미리 추출한다.
id=transport['id']
x=transport[['BRT','광역버스','지선버스','간선버스','마을버스','역 터미널']]

# PCA를 활용하여 지수를 만드는 것이기에, n_components 1로 고정.
pca= PCA(n_components = 1)
PC=pca.fit_transform(x)
result3 = pd.DataFrame(PC, columns=['PC1'])
result3['id']=id

# PCA PC1값에 minmax scaling을 해주었다. 
# 이유: 다중회귀분석 
min_max_scaler = MinMaxScaler(feature_range=(5,100))
x=result3['PC1']
x=x.to_numpy(dtype=float)
x=x.reshape(-1,1)
x1= min_max_scaler.fit_transform(x)
result3 = pd.DataFrame(x1, columns=['PC1'])
result3['id']=id 
transport_rate = result3


# ### 생활 편의 지수

# In[ ]:


# PCA 결과를 바탕으로 geo(격자) 데이터와 합쳐준다.
pca = pd.merge(life_rate,geo,on='id',how='outer')
pca = gpd.GeoDataFrame(pca)

plot_grid_map(pca, col = 'PC1', title = '생활 편의 지수', k=12,
              mode = 'cont_classify',c_mode = 'FisherJenks', colors = 'Purples', percen = False)


# ### 안전 지수

# In[ ]:


# PCA 결과를 바탕으로 geo(격자) 데이터와 합쳐준다.
pca = pd.merge(safety_rate,geo,on='id',how='outer')
pca = gpd.GeoDataFrame(pca)

plot_grid_map(pca, col = 'PC1', title = '안전 지수', k=12,
              mode = 'cont_classify',c_mode = 'FisherJenks', colors = 'Greens', percen = False)


# ### 교통 지수

# In[ ]:


# PCA 결과를 바탕으로 geo(격자) 데이터와 합쳐준다.
pca = pd.merge(transport_rate,geo,on='id',how='outer')
pca = gpd.GeoDataFrame(pca)

plot_grid_map(pca, col = 'PC1', title = '교통 지수', k=12,
              mode = 'cont_classify',c_mode = 'FisherJenks', colors = 'Blues', percen = False)

