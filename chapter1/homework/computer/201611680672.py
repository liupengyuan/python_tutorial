
# coding: utf-8

# - 练习 1：写程序，可由键盘读入用户姓名例如Mr. right，让用户输入出生的月份与日期，判断用户星座，假设用户是金牛座，则输出，Mr. right，你是非常有性格的金牛座！。

# In[1]:

name=input('what is your name ?')
print('when is you birthday ?example:5月21输入为以下各式：521')

birthday=int(input())
if 421<=birthday<=521 :
        print('Mr.',name,'你是非常有个性的金牛座!')


# - 练习 2：写程序，可由键盘读入两个整数m与n(n不等于0)，询问用户意图，如果要求和则计算从m到n的和输出，如果要乘积则计算从m到n的积并输出，如果要求余数则计算m除以n的余数的值并输出，否则则计算m整除n的值并输出。

# In[2]:

m=int(input('please enter an integer'))
n=int(input('please enter an integer'))

print('请输入您要执行的操作：+、*、%、else')
operation=input()

if operation=='+':
    print(m+n)
elif operation=='*':
    print(m*n)
elif  operation=='%':
    print(m%n)
else :
    print(n//m)
    


# - 练习 3：写程序，能够根据北京雾霾PM2.5数值给出对应的防护建议。如当PM2.5数值大于500，则应该打开空气净化器，戴防雾霾口罩等

# In[3]:

value=int(input('请输入今天北京PM2.5的值'))

if value>500:
    print('建议打开空气净化器，出门戴口罩')


# - 练习 4：英文单词单数转复数，要求输入一个英文动词（单数形式），能够得到其复数形式，或给出单数转复数形式的建议（提示，some_string.endswith(some_letter)函数可以判断某字符串结尾字符，可尝试运行：'myname'.endswith('me')，'liupengyuan'.endswith('n')`）。

# In[6]:

word=input('please enter a word ')

if word.endswith('s') or word.endswith('x') or word.endswith('ch') or word.endswith('sh') or word.endswith('o') :
    print(word,'es',sep='')
else :
    print(word,'s',sep='')       # 此题不全面，若为一辅音字母加Y用现学方法怎解决？


# - 尝试性练习：写程序，能够在屏幕上显示空行。

# In[8]:

print('name')
print(sep='\n')
print('name')


# In[10]:

n=int(input('请输入将输入的数字总个数'))
max_num=int(input('请输入一个整数'))
secmax_num=int(input('请输入一个整数'))
i=2

while i<n :
    if max_num<secmax_num :
        temp1=max_num
        max_num=secmax_num
        secmax_num=temp1
    num=int(input('请输入一个整数'))
    if num>max_num :
        temp2=max_num
        max_num=num
        secmax_num=temp2
    elif num>secmax_num :
        secmax_num=num
    i+=1
print('The max nummber is :',max_num)
print('The second max number is',secmax_num)
        

