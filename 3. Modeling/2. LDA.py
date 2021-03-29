#!/usr/bin/env python
# coding: utf-8

# ## 2) LDA
# 
# - NLP 토픽 모델링의 대표적인 알고리즘
# 
# - 문서의 집합들을 바탕으로 하며, 단어가 특정 토픽에 존재할 확률과 문서에 특정 토픽이 존재할 확률을 결합확률로 추정하여 문서 내에 어떤 토픽들이 존재하는지 알아내는 알고리즘

# ### Modeling

# In[ ]:


import gensim
from gensim import corpora
import pyLDAvis.gensim


# In[ ]:


def ldamodel(df, n=4):
    # 토큰 추출
    token = df['token']
    dictionary = corpora.Dictionary(token)
    corpus = [dictionary.doc2bow(text) for text in token]
    
    #LDA 모델 훈련시키기
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = n, id2word=dictionary, passes=15)
    pyLDAvis.enable_notebook()
    vis = pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary)
    return vis


# ### 2017년 4월 1일 ~ 6월 30일
# 
# - 대선 주자들의 세종시 관련 공약들로 인해 세종시 주택시장에 대한 관심이 증폭되던 시기
# 
# - 세종시 주택 매매량이 증가하고 아파트 거래가 상승 폭을 보인 시기
# 
# - 아파트 거래와 동시에 인구의 유입도 많았던 시기

# In[ ]:


pyLDAvis.display(ldamodel(df_2))


# ### 2017년 7월 1일 ~ 10월 31일
# 
# - 문재인 정권의 8.2 부동산 정책이 시행되었던 시기  
# - 세종시 주택 매매 거래량이 감소하고 특히 아파트 거래가 하락 폭을 보인 시기  
# - 인구의 유입도 점차 줄어들던 시기  

# In[ ]:


pyLDAvis.display(ldamodel(df_3, n=3))


# ### 2019년 10월 1일 ~ 12월 31일
# - 전국의 주택 시장이 상승장의 모습을 띄었던 시기  
# - 세종시 주택 거래 중 매매거래가 폭등하고, 전월세 거래 또한 상승세의 시기  
# - 폭발적으로 늘어난 주택 거래량과는 달리 순유입자수 증가율은 오히려 감세를 보였다는 점이 특징

# In[ ]:


pyLDAvis.display(ldamodel(df_8))


# ### 2020년 5월 1일 ~ 7월 31일
# - 전국의 주택 시장이 상승장의 모습을 띄었던 시기  
# - 세종시 주택 거래 중 매매거래가 폭등하고, 전월세 거래 또한 상승세의 시기
# - 폭발적으로 늘어난 주택 거래량과는 달리 순유입자수 증가율은 오히려 감세를 보였다는 점이 특징

# In[ ]:


pyLDAvis.display(ldamodel(df_10, n=3))


# In[ ]:




