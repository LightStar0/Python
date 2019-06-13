#!/usr/bin/env python
# coding: utf-8

# # Python 的 lambda函數

# In[1]:


def circle(radius):
    return radius * radius * 3.14

print(circle(10))


# In[2]:


def max(m,n):
    return m if m > n else n
print(max(10,3))


# In[4]:


#lambda寫法
max = lambda m,n: m if m>n else n
print(max(10,3))


# In[8]:


#list * 5
a = [1,2,3,4,5]
print(a*5)
#numbpy * 5
import numpy as np
b=np.array(a)
print(b*5)
#lamda寫法
c=list(map(lambda x: x*5, a)) #map(function, data)
print(c)


# In[9]:


def circle(radius):
    return radius * radius * 3.14

print(circle(10))


# # 錯誤處理 try: except:

# In[10]:


def circle(radius):
    try:
        return radius * radius * 3.14
    except:
        return "請輸入數值"
print(circle(10))
print(circle('十'))


# In[ ]:




