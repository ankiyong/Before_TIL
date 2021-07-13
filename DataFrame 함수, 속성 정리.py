#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[7]:


np.random.seed(3)
df = pd.DataFrame(np.random.randint(3,size = [4,4]))
df


# In[12]:


df.index.name = 'a'


# In[13]:


df.columns.name = 'b'
df


# In[10]:


df.values


# In[14]:


df.shape


# In[15]:


df.info()


# In[28]:


df.describe()


# In[31]:


df


# In[37]:


df[1:4]


# In[38]:


df.sum()


# In[42]:


df.mean()
df.mean(axis = 1)


# In[40]:


df.max()
df.max(axis = 1)


# In[41]:


df.min()
df.min(axis =1)


# In[44]:


df.drop(1,1) #1 열 삭제
df.drop(1,0) #1 행 삭제


# In[45]:


df.dropna(axis = 0) #nan값이 포함된 행 삭제


# In[46]:


df.dropna(axis = 1) #nan값이 포함된 열 삭제


# In[47]:


df.set_index(1)


# In[48]:


df.reset_index(drop = True)


# In[49]:


df.reset_index()


# In[50]:


df.rename(index = {1:'z'})


# In[53]:


df.rename(columns={1:'x'})


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




