#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow


# In[2]:


#這是單行註解
'''
這是多行註解
'''
a=3
b=8
print(a+b)


# In[3]:


a=3
b=8
a,b=b,a
print(a)
print(b)


# In[1]:


x,y,z=3,4,5
print(x)
print(y)
print(z)


# In[3]:


x,y,z=3,4,5
x += 1
y *= 2
z **= 3
print(x,y,z)


# In[4]:


#變數的應用
#Q:邊長為3,4,5的三角形，其面積大小為何?


# In[5]:


import math
a = math.sqrt(((3+4+5)/2)*(((3+4+5)/2)-3)*(((3+4+5)/2)-4)*(((3+4+5)/2)-5))
print(a)


# In[6]:


import math
a,b,c=3,4,5
s=(a+b+c)/2
d=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(d)


# In[7]:


#python動態類型變數，使用前不需要宣告資料型態


# In[8]:


x=254
print(type(x))


# In[9]:


x=254
print(type(x))
id(x)


# In[10]:


x='write'
print(type(x))
id(x)


# In[12]:


#數值資料的計算


# In[13]:


#半徑為4.5的圓錐體面積為何?
import math
print((4.5*4.5*math.pi*4.5)/3)


# In[14]:


x=16
y=3
print(x/y)
print(x//y)#求商
print(x%y)#求餘數


# In[15]:


#關係運算
x=10
print(20==20)
y=20
print(x==y)
x=y
print(x)


# In[16]:


#級聯比較
a,b,c=10,20,30
print(a<=b<=c)


# In[17]:


x=3.141592627
print(x-3.14)


# In[19]:


#邏輯運算 以閏年為例
y=2010
print(y%4==0 and y%100!=0 or y%400==0)
y=2012
print(y%4==0 and y%100!=0 or y%400==0)
y=2000
print(y%4==0 and y%100!=0 or y%400==0)


# In[21]:


#型態轉換
x=12
y=float(x)+0.5
print(y)
print(int('123'))
print(float('123'))
print(int(123.333))
x=10*3.25 #32.5
y=200*200 #40000
s=' The value of x is ' + str(x) + ' and y is ' +str(y)
s1 =' The value of x is ' + repr(x) + ' and y is ' +repr(y)
print(s)
print(s1)


# In[22]:


#非內置模組
import math
print(math.pi)
print(math.pow(2,3))
print(8.3*10.58*math.sin(37.0/180*math.pi)/2)
print(math.sqrt(25))


# In[23]:


#算園面積
import math
r=input("請輸入半徑:")
area=float(r) * float(r) * math.pi
print(area)


# In[ ]:




