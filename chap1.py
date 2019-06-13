#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=3
b=5
a+b


# # Python 利用 requests 模組產生 HTTP請求

# In[3]:


import requests
c = requests.get("https://blog.xuite.net/smpss94181/smpss94181?st=c&p=1&w=0")
print(c.text)


# In[6]:


from skimage import io,data
img=data.astronaut()
dst=io.imshow(img)
print(type(dst))
io.show


# In[ ]:





# In[ ]:




