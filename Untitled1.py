#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import jieba


# In[12]:


data=pd.read_csv(r'F:\Test\2019-Dec.csv',nrows=10000)


# In[13]:


print(data.head())
print(data.shape)
print(data.info())


# In[ ]:




