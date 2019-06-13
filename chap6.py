#!/usr/bin/env python
# coding: utf-8

# # while迴圈
# ## 1+2+3+...+10的總和

# In[ ]:


sum = 0
count = 1
while count <=10:
    sum = sum + count #sum +=count
    count +=1 #count=count +1
print('1+2+2+...+10=',sum)


# # 銀行利息範例 

# In[ ]:


x = 10000
year = 0
while x < 20000:
    year +=1
    x = x * 1.0104
print(str(year),"年後，存款金額會加倍")


# # 帳號密碼程式 

# In[ ]:


id = 'tony'
pwd = '1234'
while True:
    x = input('請輸入帳號:')
    y = input('請輸入密碼:')
    if(x==id and y==pwd):
        print('歡迎登入')
        break
    else:
        print('帳號/密碼輸入錯誤')


# # break, continue,pass範例 

# In[ ]:


mylist = ['c#','Python','Java','C++']
for i in mylist:
    if i == 'Java':
        break
    else:
        print(i)


# In[ ]:


mylist = ['c#','Python','Java','C++']
for i in mylist:
    if i == 'Java':
        continue
    else:
        print(i)


# In[ ]:


mylist = ['c#','Python','Java','C++']
for i in mylist:
    if i == 'Java':
        pass
    else:
        print(i)


# In[ ]:


import random
for i in range(0,10):
    print(random.random())


# In[ ]:


import random
for i in range(0,10):
    print(random.randint(1,10))


# In[2]:


import random
number = random.randint(1,99)
while True:
    guess = input('請輸入1-99的數字(q離開):')
    if guess == 'q':
        print('離開遊戲，正確數字是',number)
        break
    else:
        if number==int(guess):
            print('恭喜，猜對了')
            break
        else:
            print('猜錯了')


# In[ ]:




