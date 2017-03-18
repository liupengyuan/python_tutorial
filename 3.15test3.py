m=int(input('请输入一个整数：'))
sum=0
while m:
    sum=sum+m
    m=int(input('请输入一个整数，如若不想再输入了则输入0：'))
print('和为：',sum)
