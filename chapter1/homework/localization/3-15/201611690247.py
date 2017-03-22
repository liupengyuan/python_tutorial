
# coding: utf-8

# ## 练习2

# In[7]:

name=input('请输入你的名字')
print('你好（～￣▽￣～）',name)

n=0
total=0
number=int(input('请输入你即将输入的整数个数'))

while n<number:
    i=int(input('请输入一个整数'))
    total=total+i
    n=n+1
    
print('你输入的整数之和为',total)
print('再见\("▔□▔)/\("▔□▔)/\("▔□▔)/',name)


# 
# ## 练习3

# In[8]:

name=input('请输入你的名字')
print('你好（～￣▽￣～）',name)

n=input('你想要输入一个数字吗？（请输入yes／no）')
while n=='yes':
    input('请输入一个数字')
    n=input('你想要输入一个数字吗？（请输入yes／no）')

print('不想输就算了吧（╯－＿－）╯╧╧  ')
print('谢谢使用，再见\("▔□▔)/\("▔□▔)/\("▔□▔)/',name)


# 
# ## 练习4

# In[9]:

name=input('请输入你的名字')
print('你好（～￣▽￣～）',name)

total=0
pro=1

n=int(input('请输入一个数字'))
total=total+n
pro=pro*n

while total>=n or pro>=n**2:
    total=total+n
    pro=pro*n
    n=int(input('请输入一个数字'))
    
print('你当前输入所有数字的和比当前输入数字小，且输入所有数字的积比当前输入数字的平方小')

print('程序已结束(*ﾟ▽ﾟ*) ，谢谢使用',name)


# In[ ]:



