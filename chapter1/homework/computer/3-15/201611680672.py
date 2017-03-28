
# coding: utf-8

# - 练习2：由用户指定整数个数，并由用户输入多个整数，并求和的代码

# In[7]:

n=input('请输入将计算的整数个数，以回车结束')
n=int(n)
i=1
sum=0

while i<=n:
    y=input('请输入一个需计算的数字')
    y=int(y)
    sum+=y
    i+=1
    
print('这几个数字的和为：')
print(sum)


# - 练习3：用户可以输入任意多个数字，直到用户不想输入为止

# In[8]:

print('请输入任意数字，直道您不想输入为止，请输入f并回车结束')

while True :
    i=input()
    if i=='f' :    #atention:不可以敲成：i==f
        break


# - 练习4：用户可以输入任意多个数字，直到输入的所有数字和比当前输入的数字小，且输入的所有的数字的积比当前输入的数字的平方小

# In[5]:

print('请输入任意数字')
sum=0
total=1

while True :
    i=input()
    i=int(i)
    if i>sum and i**2 >total :
        break
    sum+=i
    total*=i
   
    

