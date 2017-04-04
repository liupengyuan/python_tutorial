
# coding: utf-8

# ## 练习1

# In[1]:

name=input('请输入你的名字')
print('hello',name)
bir=int(input('请输入你的生日 例：1202（12月2日）115（1月15日）'))

if bir>=1222:
    print(name,'你是执着现实的摩羯座')
elif bir>=1123:
    print(name,'你是自由乐观的射手座')
elif bir>=1024:
    print(name,'你是神秘敏锐的天蝎座')
elif bir>=923:
    print(name,'你是公平和谐的天秤座')
elif bir>=823:
    print(name,'你是完美理性的处女座')
elif bir>=723:
    print(name,'你是骄傲威严的狮子座')
elif bir>=622:
    print(name,'你是敏感柔情的巨蟹座')
elif bir>=521:
    print(name,'你是花心多变的双子座')
elif bir>=420:
    print(name,'你是稳健固执的金牛座')
elif bir>=321:
    print(name,'你是热情活力的白羊座')
elif bir>=219:
    print(name,'你是浪漫梦幻的双鱼座')
elif bir>=120:
    print(name,'你是自由博爱的水瓶座')
else:
    print(name,'你是执着现实的摩羯座')


# ## 练习2

# In[10]:

m=int(input('请输入一个不为零的整数'))
n=int(input('请输入一个比上一整数小的非零整数'))

attempt=input('请您选择以下选项中的一个指令。A.连续加和 B.连续乘积 C.余数计算 D.整除计算')

total=n
product=n
if attempt=='A':
    while n<m:
        n=n+1
        total+=n
    print('连续加和结果为',total)

elif attempt=='B':
    while n<m:
        n=n+1
        product*=n
    print('连续乘积结果为',product)

elif attempt=='C':
    remainder=m%n
    print('余数计算结果为',remainder)

else:
    divide=m//n
    print('整除计算结果为',divide)


# ## 练习3

# In[11]:

pm=int(input('请输入空气质量指数'))

if pm>300:
    print('空气严重污染，请尽量不要到室外活动')

elif pm>200:
    print('空气重度污染，请减少室外活动')
    
elif pm>150:
    print('空气中度污染，请打开空气净化器')
    
elif pm>100:
    print('空气轻度污染，在室外活动请佩戴口罩')
    
elif pm>50:
    print('空气质量良，可以进行适当的室外活动')
    
else:
    print('空气质量优，快到室外去呼吸一下新鲜空气吧')


# ## 练习4

# In[39]:

word=input("请输入一个英文名词")
if word.endswith('y'):
    print("把y删去，变成ies。",word,'(ies)',sep='')
elif word.endswith('sh'):
    print("直接在结尾加es。",word,'es',sep='')
elif word.endswith('to'):
    print("o结尾有生命加es，无生命加s。",word,'es',sep='')
elif word.endswith('f'):
    print("将f、fe删去，变成ves。",word,'(ves)',sep='')
else:
    print("一般情况直接加s",word,'s',sep='')


# ## 尝试性练习

# In[5]:

print(                    )
print('上面是空行')


# ## 挑战性练习

# In[ ]:

max_number = int(input('请输入一个整数，回车结束'))

i = 0
while i < 10:
    i += 1
    n = int(input('请输入一个整数，回车结束'))
    if n > max_number:
        max_number = n

print('最大值是：', max_number)


# In[ ]:



