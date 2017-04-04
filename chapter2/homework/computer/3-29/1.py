# -*- coding: utf-8 -*-


"""
Spyder Editor

This is a temporary script file.
"""
#星座
a=input('pls insert your name ')
print('hello',a)
b=int(input('pls insert your birth month:'))
c=int(input('pls insert your birth date:'))
t='You are a'
B='金牛座'
C='白羊座'
D='金牛座'
F='双子座'
G='巨蟹座'
H='狮子座'
E='处女座'
I='天秤座'
J='天蝎座'
K='射手座'
L='摩羯座'
M='水瓶座'
N='双鱼座'


if b==1:
    if c>=20 and c<=31:
        print(t,M)
    else:print(t,C)
if b==2:
    if c>=19 and c<=29:
        print(t,N)
    else:print(t,M)
if b==3:
    if c>=21 and c<=31:
        print(t,C)
    else:print(t,N)
if b==4:
    if c>=20 and c<=30:
        print(t,D)
    else:print(t,C)
if b==5:
    if c>=21 and c<=31:
        print(t,F)
    else:print(t,D)
if b==6:
    if c>=22 and c<=30:
        print(t,G)
    else:print(t,F)
if b==7:
    if c>=23 and c<=31:
        print(t,H)
    else:print(t,G)
if b==8:
    if c>=23 and c<=31:
        print(t,E)
    else:print(t,H)
if b==9:
    if c>=23 and c<=30:
        print(t,I)
    else:print(t,E)
if b==10:
    if c>=24 and c<=30:
        print(t,J)
    else:print(t,I)
if b==11:
    if c>=23 and c<=30:
        print(t,K)
    else:print(t,J)
if b==12:
    if c>=22 and c<=30:
        print(t,C)
    else:print(t,K)


#写程序，可由键盘读入两个整数m与n(n不等于0)，询问用户意图，
#果要求和则计算从m到n的和输出，如果要乘积则计算从m到n的积并输出，
#如果要求余数则计算m除以n的余数的值并输出，否则则计算m整除n的值并输出。
m=int(input("Input m:"))
n=int(input("Input n:"))
b=(input('a:add b:product c:mod d:divide \n pls choose a b c or d :'))
if (n==0):
    {print("n==0 error")}
elif (b=='a'):
    print(m+n)
elif (b=='b'):
    print(m*n)
elif (b=='c'):
    print(m%n)
elif (b=='d'):
    print(m/n)   

#pm2.5
pm=int(input("请输入pm2.5的值："))
if(pm<=500):
    print("空气还可以")
if(pm>500):
    print("空气很差，您可以打开空气净化器，戴防雾霾口罩。")
#写出单词复数
def plural(word):  
    if word.endswith('y'):  
        return word[:-1] + 'ies'  
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:  
        return word + 'es'  
    elif word.endswith('an'):  
        return word[:-2] + 'en'  
    else:  
        return word + 's'
a=input("pls input a word:")
print("复数是:",plural(a))

        

