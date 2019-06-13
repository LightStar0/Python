#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Python物件
list, tuple, dict, sets
list: [1, 2, 3]
tuple:(1, 2, 3) #不能改變其值
dict:{1:'apple',2:'banana',3:'orange'}
sets:{apple, banana, orange}


# In[4]:


#list串列
my_list0 = [1,2,3]
print(my_list0)


# In[5]:


#list串列
my_list0 = [1,2,3]
print(my_list0)
my_list1 = ['python', 'js', 'SQL']
print(my_list1[0])
my_list1.append('java')#附加於最後的位置
print(my_list1)
#新增至特定位置


# In[6]:


#新增至特定位置
my_list1.insert(0,'c#')
print(my_list1)
#list長度
print(len(my_list1))


# In[7]:


my_list2 = ['c#', 'python', 'js', 'SQL', 'java']
#list長度
print(len(my_list2))
print(len(my_list2[1]))


# In[8]:


#list刪除
my_list3 = ['c#', 'python', 'js', 'SQL', 'java']
my_list3.remove('js')#刪除某特定的物件
print(my_list3)
del my_list3[0]#刪除某特定位置的物件
print(my_list3)
del my_list3[-1]#-1刪除從後面數來第一個
print(my_list3)


# In[9]:


#檢查是否存在
print('java' in ['python', 'js', 'c#'])


# In[10]:


#串列的重複
a=[1,2]
print(a*5)


# In[11]:


#串列取值
a=[1,2,3,4,5,6,7,8,9]
b=a[0:3] #包含0，但是不包含3
print(b)
c=a[0:3:2]#間隔取值 [開始:結束:間隔]
print(c)
del a[7:9]
print(a)
print(max(a))#最大值
print(min(a))#最小值
print(a.index(1))#1出現的索引值
print(a.count(1))#出現的次數


# In[12]:


print(a)
a.reverse()#串列反轉
print(a)
a.sort()#串列排序
print(a)


# In[13]:


a=[123,'abc',[111,222],[333,444]]
print(a[0])
print(a[1])
print(a[2])
print(a[2][1])


# In[14]:


a=[111,222] + [333,444] + [555,666]
print(a)


# In[15]:


#串列list常用在for迴圈
shoplist = ['milk','egg','coffee','wetermelon']
for item in shoplist:
    print(item)


# In[ ]:


#tuple(元組)
tuple的元素不准新增、刪除或修改


# In[16]:


a_list = ['python','js','c#']
a_tuple = ('python', 'js', 'c#')
b_tuple = tuple(a_list)
print(type(a_list))
print(type(a_tuple))
print(b_tuple)


# In[17]:


c_tuple = 111,222,333 #c_tuple=(111,222,333)
print(c_tuple)
print(type(c_tuple))


# In[ ]:


dict (字典 - dictionary)
帶有鍵值(key)的list


# In[19]:


a_list = ['python','js','c#']
a_dict = {0:'python',1:'js',3:'c#'}
print(a_list[0])
print(a_dict[0])
b_dict = {'lst':'python','2nd':'js','3rd':'c#'}
print(b_dict['lst'])


# In[ ]:




