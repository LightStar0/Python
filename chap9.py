#!/usr/bin/env python
# coding: utf-8

# # 雲端載入

# In[5]:


import pandas as pd

url="http://storage.googleapis.com/2017_ithome_ironman/data/iris.csv"

iris_df = pd.read_csv(url)#iris資料統計－鴛尾花  Setosa、Versicolour、Virginica
iris_df.head()#鳶尾花的「萼片長」、「萼片寬」、「花瓣長」、「花瓣寬」


# In[3]:


iris_df.mean()#平均


# In[4]:


iris_df['Sepal.Length'].median()


# # 本地端載入

# In[7]:


import pandas as pd
iris_df=pd.read_csv('iris.csv')
iris_df.head()


# # excel檔案載入

# In[8]:


import pandas as pd
url="http://storage.googleapis.com/2017_ithome_ironman/data/iris.xlsx"

iris_df = pd.read_excel(url)#iris資料統計－鴛尾花  Setosa、Versicolour、Virginica
iris_df.head()#鳶尾花的「萼片長」、「萼片寬」、「花瓣長」、「花瓣寬」


# # 自訂函數

# In[9]:


import math
def circle(radius):
    area = radius * radius * math.pi
    return area
print(circle(10))


# # 自訂函數(輸入模式)

# In[12]:


import math

def circle(radius):
    area = radius * radius * math.pi
    return area
r=input("請輸入圓的半徑：")
print("圓面積為：",circle(float(r)))


# # example: exchange sort 排序

# In[13]:


import random

my_vector = random.sample(range(0,100),10)
print(my_vector)


# # 從大排到小

# In[16]:


import random

def exchange_sort(input_list):
    a=input_list
    for i in range(0,len(input_list)-1):
        for j in range(i+1,len(input_list)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a
my_vector = random.sample(range(0,100),10)
print(my_vector)
print(exchange_sort(my_vector))


# # 從小排到大

# In[17]:


import random

def exchange_sort(input_list):
    a=input_list
    for i in range(0,len(input_list)-1):
        for j in range(i+1,len(input_list)):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]
    return a
my_vector = random.sample(range(0,100),10)
print(my_vector)
print(exchange_sort(my_vector))


# In[ ]:




