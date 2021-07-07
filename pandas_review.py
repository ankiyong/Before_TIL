#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[10]:


s1 = pd.Series([1,2]) #2개 이상의 원소 값을 갖는 시리즈 생성시 list tuple dict 사용
s1


# In[12]:


s1 = pd.Series([1,2,2.3,2.3]) #서로 다른  type의 원소를 갖는 list를 활용한 시리즈
s1


# In[14]:


s2 = pd.Series([1,2,'a','b']) #숫자와 문자가 혼용되면 문자 형태로 시리즈 생성
s2 


# - 범위를 series의 value 생성하는데 사용하기 - range() / np.arange()

# In[15]:


s = pd.Series(range(10,14))
s


# In[17]:


s = pd.Series(np.arange(200))
s


# - 결측값을 포함해서 series를 만들기
#     - 결측값은 NaN : numpy라는 모듈의 nan 속성을 통해서 생성 가능 -> np.nan

# In[19]:


s = pd.Series([1,2,3,np.nan,6,7]) #결측값이 포함되면 float형으로 처리된다
s


# - index를 명시해서 series 만들기
#     - 숫자 index지정/문자 index지정 가능
#     - 변수 = pd.Series([값1,값2,...,값n],index=[index1,index2,index3,...,n])
#    

# In[22]:


s = pd.Series([10,20,30],index=['1','2','3']) #index명시해서 시리즈 생성(수치인덱스)
s


# In[23]:


s = pd.Series([10,20,30],index=['a','b','b']) #index명시해서 시리즈 생성(문자 인덱스)
s


# In[27]:


s.index


# - index 활용 : 
#     - series의 index는 index속성으로 접근
# - series.index.name 속성
#     - series의 index에 이름을 붙일 수 있음

# In[29]:


s.index.name = '항목' #인덱스에 이름을 붙임
s


# In[30]:


s= pd.Series([9904312,3448737,289045,2466052],
            index=["서울","부산","인천","대구"])
s.index


# In[31]:


s.index.name = '지역'
s


# - series의 실제 값 추출 => series.values 속성 사용

# In[33]:


s.values #시리즈의 값에 해당하는 부분을 array로 반환


# ##### 딕셔너리로 시리즈 만들기
# - Series({key:value,key1:value1....})
# - 인덱스 -> key
# - 값 -> value
# - key가 index로 처리 되므로 명시적으로 index를 설정하게 된다

# In[34]:


s = pd.Series({'name':'kim','age':25}) #key가 인덱스 역할을 하게된다
s


# In[36]:


city = {'서울' : 9639399, '부산':3392939,'인천':2639403,'대전':1490303}
s = pd.Series(city) #dict를 변수에 담아 시리즈로 만드는것도 가능하다
s


# - 딕셔너리의 원소는 순서를 갖지 않는다.
#     - 딕셔너리로 생성된 시리즈의 원소도 순서가 보장되지 않는다.
#     - 만약 순서를 보장하고 싶으면 인덱스를 리스트로 지정해야 한다.
# 

# In[37]:


s2 = pd.Series(city,index=['부산','인천','서울','대전'])
s2


# In[38]:


s[0] #s시리즈의 0번 인덱스에 담긴 서울 값이 반환된다


# In[39]:


s['서울'] #문자인덱스의 경우 이름을 직접 기입하여 해당 값을 반환하는 것이 가능하다


# In[40]:


#확인문제
s_1 = pd.Series([1,2,3],index=[1,2,3])
s_1


# In[44]:


s_1[0] #인덱스의 종류가 정수형이면 위치 인덱스 사용이 불가능하다
       #라벨 인덱스와 마찬가지로 해당 인덱스의 이름을 기입해야 한다


# In[45]:


s #한줄에 위치,라벨인덱스를 동시에 접근 가능
s[3],s['대전'] #해당 값을 tuple로 반환한다


# #### list이용 indexing
#     - 자료의 순서를 바꿔 반환하거나, 특정 자료 여러개를 선택할 때 사용
#     - 시리즈명[[index1,index2,...]]

# In[51]:


s[[0,2,1]] #괄호를 두번 넣어야한다


# In[49]:


s[['서울','인천']]


# ##### 시리즈 슬라이싱을 이용한 인덱싱
# - 정수형 위치 인덱스를 사용한 슬라이싱
#     - 시리즈[start:stop+1]
#     
#     
# - 문자(라벨)인덱스 이용 슬라이싱
#     - 시리즈['시작라벨':'끝라벨']  : 표시된 라벨 범위 모두 추출
# 

# In[52]:


s


# In[53]:


s[1:3] #시리즈[str:stop+1]


# In[54]:


s['부산':'대전'] #라벨 인덱스를 이용한 슬라이싱도 가능하다


# In[55]:


s_test = pd.Series([1,2,3],index=[6,7,8])
s_test


# In[56]:


s_test[1:5] #명시적으로 설정한 정수 인덱스를 슬라이싱 하면 위치 슬라이싱이 적용된다


# In[57]:


s.서울 #문자인덱스는 .를 이용해 접근이 가능하다


# In[58]:


s_test.1 #.연산자를 이용한 원소 접근은 문자 인덱스만 가능하다


# #### indexing을 통한 data 업데이느
#     -시리즈명[index] = data값

# In[59]:


s['서울'] = 10000000 #dict 생성 방법과 유사
s  


# #### index 재사용 가능

# In[63]:


s.index
s1 = pd.Series(np.arange(4),s.index)
s1


# ## series 연산

# ##### 벡터화 연산
# - numpy 배열처럼 pandas의 시리즈도 벡터화 연산 가능 
# - 벡터화 연산이란 집합적 자료형의 원소 각각을 독립적으로 계산을 진행하는 방법
#     - 단, 연산은 시리즈의 값에만 적용되며 인덱스 값은 변경 불가
# 

# In[64]:


pd.Series([1,2,3]) * 3 #시리즈 내 각각의 요소에 동일한 연산을 적용해 값을 반환한다


# In[66]:


s / 1000000 #시리즈 명을 직접 연산에 사용할 수도 있다


# #### **Boolean selection**
#   - boolean Series가 []와 함께 사용되면 True 값에 해당하는 값만 새로 반환되는 Series객체에 포함됨
#   - 다중조건의 경우, &(and), |(or)를 사용하여 연결 가능
# 

# In[72]:


s0 = pd.Series(np.arange(10),np.arange(10)+1) #인덱스와 값의 개수는 동일해야한다 
s0                                            #그래서 11이 아니고 +1을 추가하는것 


# In[73]:


s0[s0>6] #6을 초과하는 값 반환


# In[74]:


s0[s0%2==0] #짝수값 반환


# In[75]:


s0[s0.index>5] #인덱스값이 5를 초과하는 값 반환


# In[76]:


(s0>7).sum() #7을 초과하는 값의 개수 반환


# In[77]:


s0[s0>=7].sum() #출력되는 원소 값을 모두 더한 값을 반환


# ### 두 시리즈 간의 연산

# In[80]:


num_s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
num_s2 = pd.Series([5,6,7,8],index=['b','c','d','a'])
num_s1
num_s2


# In[81]:


num_s1 + num_s2


# In[86]:


num_s3 = pd.Series([1,2,3,4],index=['e','b','f','g'])
num_s4 = pd.Series([5,6,7,8],index=['b','c','d','a'])
num_s3
num_s4


# In[83]:


num_s3 + num_s4 #동일한 인덱스 값을 찾지 못하면 결측값을 출력


# In[96]:


num_s3.values + num_s4.values #values 속성을 사용하면 시리즈의 형태가 사라져 동일한 위치의 원소들
#끼리 연산을 진행


# ##### 딕셔너리 와 시리즈의 관계
# - 시리즈 객체는 라벨(문자)에 의해 인덱싱이 가능
# - 실질적으로는 라벨을 key로 가지는 딕셔너리 형과 같다고 볼 수 있음
# - 딕셔너리에서 제공하는 대부분의 연산자 사용 가능
#     - in 연산자 : T/F
#     - for 루프를 통해 각 원소의 key와 value에 접근 할수 있다.
# 

# In[97]:


'서울' in s


# In[100]:


s.items() #dict와 유사하게 list개체로 반환하면 값을 볼 수 있다
list(s.items())


# In[106]:


for i,j in s.items(): 
    print('%s=%d' % (i,j))


# #### 시리즈 데이터의 갱신/추가/삭제
# - 인덱싱을 사용하면 딕셔너리 처럼 갱신 추가

# In[107]:


s['부산'] = 3000000 #시리즈의 값을 수정
s


# In[109]:


s['대구'] = 3000001 #시리즈에 새로운 데이터 추가
s


# In[110]:


del s['대전'] #시리즈의 값을 제거
s


# In[ ]:





# In[ ]:




