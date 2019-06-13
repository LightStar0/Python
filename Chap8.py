#!/usr/bin/env python
# coding: utf-8

# # Pandas Data Frame

# In[1]:


import pandas as pd

groups = ["Modern Web","DevOps","Cloud","Big Data","Security","自我挑戰組"]
ironmen = [59,9,19,14,6,77]
ironmen_dict = {
    "groups":groups,#索引列
    "ironmen":ironmen#資料列
}
ironmen_df = pd.DataFrame(ironmen_dict)
ironmen_df


# In[2]:


print(ironmen_df.ndim)#看維度
print(ironmen_df.shape)#看形狀
print(ironmen_df.dtypes)#看型態


# In[3]:


print(ironmen_df.sum()) #總和(文字會加在一起)
print(ironmen_df.ironmen.sum())#單獨
print(ironmen_df.mean())#平均
print(ironmen_df.median)#中位數
print(ironmen_df.describe())#描述


# In[5]:


import pandas as pd
import numpy as np

groups = ["Modern Web","DevOps",np.nan,"Cloud","Big Data","Security","自我挑戰組"]
ironmen = [59,9,19,14,6,77,np.nan]
ironmen_dict = {
    "groups":groups,#索引列
    "ironmen":ironmen#資料列
}
ironmen_df = pd.DataFrame(ironmen_dict)
print(ironmen_df.loc[:,"groups"].isnull())#判斷哪些組的組名是遺失值
print(ironmen_df.loc[:,"ironmen"].notnull())#判斷那些組的鐵人數不是遺失值   notnull=不是空值


# In[6]:


a = ironmen_df.dropna()#刪除空值  (空值把它印出來)
b = ironmen_df.fillna(0)#空值補0  空值想要補多少
c = ironmen_df.ironmen.fillna(ironmen_df.mean())
#空值補平均數


# In[7]:


import pandas as pd

groups = ["Modern Web","DevOps","Cloud","Big Data","Security","自我挑戰組"]
ironmen  = [59,9,19,14,6,77]
#建立 data frame
ironmen_df = pd.DataFrame(ironmen,columns = ["ironmen"],index = groups)
ironmen_df


# In[8]:


import pandas as pd

groups = ["Modern Web","DevOps","Cloud","Big Data","Security","自我挑戰組"]
ironmen  = [59,9,19,14,6,77]
#建立 data frame
ironmen_df = pd.DataFrame(ironmen,columns = ["ironmen"],index = groups)
ironmen_df.sort_index()


# In[9]:


ironmen_df.sort_values(by = "ironmen")


# In[ ]:




