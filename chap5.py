#!/usr/bin/env python
# coding: utf-8

# # 第三章 流程控制 

# In[6]:


celsius=float(input('請輸入攝氏溫度:'))
fahrenheit=(9/5) * celsius + 32
print('華氏溫度為:',fahrenheit)


# In[7]:


import statistics as st
sample=[5,8,9,6,4,1,2,3,5,6]
print('樣本=', sample)
print('平均數=', st.mean(sample))
print('最大數=', max(sample))
print('最小數=', min(sample))
print('變異數=', round(st.variance(sample),2))
print('標準差=', round(st.stdev(sample),2))


# # if 

# In[11]:


numA = 3
numB = 4
if numA < numB:
    print('numB是比較大的數')


# In[12]:


numA = int(input('請輸入numA:'))
numB = int(input('請輸入numB:'))
if numA < numB:
    print('numB是比較大的數')
elif numA > numB:
    print('numA是比較大的數')
else:
    print('numA跟numB相同大小')


# # for 迴圈 

# In[13]:


sum = 0
for i in range(1,11):
    sum = sum + i
print('總和:',sum)


# In[16]:


sample = [5,8,9,6,4,1,2,3,5,6]
sum = 0
for i in sample:
    sum = sum + i
print('總和:',sum)


# # In-class exercise 隨堂練習
#     雞兔問籠問題進行求解。若共有35個頭，94隻腳，問共有幾隻雞?幾隻兔?

# In[17]:


head = 35
leg = 94
for rabbit in range(0,head+1):
    chicken = head-rabbit
    if((rabbit*4 + chicken*2) == 94):
        print('雞有',chicken, '隻')
        print('兔子有',rabbit, '隻')


# In[18]:


mylist = 'I Love Avenger IV'
for character in mylist:
    print(character)


# In[ ]:




