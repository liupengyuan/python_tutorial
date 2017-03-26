
# coding: utf-8

# In[1]:

#练习1#
n=int(input('请输入一个整数'))
i=0
total=0
while i<n:
    i=i+1
    total=total+i
print(total)


# In[2]:

'''
练习2
'''
name = input('请输入你的姓名，以回车结束。')
print('你好',name)

Num=int(input('请输入个数，以回车结束'))
i=0
total=0
while i<Num:
    i=i+1
    n=int(input('请输入一个正整数，以回车结束'))
    total=total+n
print(total)
print('再见！',name)


# In[3]:

#练习3#
name = input('请输入你的姓名，以回车结束。')
print('你好',name)

total=0
n=input('请选择是否继续输入数字，Y/N')
while n=='Y':
    m=int(input('请输入一个正整数，以回车结束'))
    total=total+m
    n=input('请选择是否继续输入数字，Y/N')

print(total)
print('再见！',name)


# In[4]:

#练习4#
name = input('请输入你的姓名，以回车结束。')
print('你好',name)

a=0 
b=1
n=int(input('请输入一个正整数，以回车结束'))
a=a+n
b=b*n
n=int(input('请输入一个正整数，以回车结束'))
while a>=n or b>=n**2:
    a=a+n
    b=b*n
    n=int(input('请输入一个正整数，以回车结束'))

print('再见！',name)


# In[ ]:



