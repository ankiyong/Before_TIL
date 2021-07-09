#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[1]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"


# In[9]:


df = pd.DataFrame([1,2,3]) #단일 list값을 df화 하면 df의 열로 추가된다
df
df = pd.DataFrame([[1,2,3],['a','b','c']]) #2차원 list를 이용해 df생성시 하위 list가 각 행으로 매핑
df


# In[10]:


df = pd.DataFrame([[1,2,3],['a','c','n'],['d','c']]) #하위 list의 원소 개수가 다를 경우 none값 저장
df


# In[14]:


df1 = pd.DataFrame({'A': [90,80,70],
                    'B': [85,98,75],
                    'C': [88,99,77],
                    'D': [87,89,86]},
                  index = ['1위','2위','3위'])
df1


# In[16]:


#df의 값을 위한 dict
data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2000002],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율":[0.0283, 0.0163, 0.0982,0.0141]
}

#열방향 인덱스(컬럼명) columns=
columns = ['지역','2015','2010','2005','2000','2010-2015 증가율']

#행방향 인덱스 index =
index=['서울','부산','인천','대구']
df2 = pd.DataFrame(data,columns = columns,index = index)
df2


# In[26]:


a = pd.Series([100, 200, 300], ['a', 'b', 'd'])
b = pd.Series([101, 201, 301], ['a', 'b', 'k'])
c = pd.Series([110, 210, 310], ['a', 'b', 'c'])
a


# In[28]:


df = pd.DataFrame([a])
df
df = pd.DataFrame([a,b,c]) 
df
#여러 시리즈를 한 리스트에 묶어 처리가 가능하며 시리즈가 추가될 때마다 df의 행값으로 추가된다


# In[31]:


train_data = pd.read_csv('../data/train.csv')
train_data.head() #불러온 자료의 상위 5개 행을 보여줌
train_data.tail() #불러온 자료의 하위 5개 행을 보여줌


# In[33]:


train_data.info() #non-Null count 열을 통해 결측값이 있는지 확인할 수 있다.


# In[37]:


train_data = pd.read_csv('../data/train.csv',index_col = 'PassengerId',usecols = ['PassengerId','Survived','Pclass','Name'])
train_data


# In[39]:


train_data.columns
train_data.index


# In[40]:


df2


# In[41]:


df2.index.name = '지역'
df2.columns.name = '특성'
df2


# In[45]:


df2.shape
df2.info()
df2.describe()


# In[46]:


df2.T


# In[55]:


df2


# In[57]:


df2['2010-2015 증가율'] = df2['2010-2015 증가율'] * 10
df2 #기존 내용 갱신


# In[60]:


df2['2005-2015증가율'] = (df2['2015']-df2['2005']) / df2['2005'] * 100
df2


# In[63]:


del df2['2010-2015 증가율'] 
df2


# In[64]:


df2


# In[66]:


df2['2015'] #시리즈 형태로 반환
df2[['2015']] #df형태로 반환


# In[75]:


df2[['2010','2000']]


# In[76]:


np.arange(12).reshape(3,4)


# In[78]:


df5 = pd.DataFrame(np.arange(12).reshape(3,4))
df5


# In[85]:


df5[[1,2]]


# In[86]:


df2.info()


# In[89]:


df2[[0:3]]


# In[90]:


df2


# In[91]:


df2[:3]


# In[92]:


df2['서울':'부산']


# In[93]:


df=pd.DataFrame(np.arange(10,22).reshape(3,4),
               index = ['a','b','c'],
               columns = ["A","B","C","D"])
df


# In[96]:


df.loc['a']


# In[127]:


df.loc['a':'b']
df.loc[['a','b']]


# In[102]:


df.loc[df.A>15]


# In[128]:


df1 = pd.DataFrame(np.arange(10,26).reshape(4,4))
df1


# In[108]:


df1.loc[1:2]


# In[112]:





# In[116]:


df.loc['a','A'] = 2
df


# In[121]:


#a행의 B C열
df.loc['a','B':'C']
df.loc[['a'],'B':'C']


# In[126]:


df.iloc[0,1]
df.iloc[0:1,0:1]
df.iloc[2,1:2]
df.iloc[1:2,3]


# In[154]:


# pd.date_range(strat='2020-1-1',periods = 3, freq = 'd')
pd.date_range(start='2018-10-7',periods=4,freq='W')

