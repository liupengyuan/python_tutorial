sum=int (input())
total=sum
while 1:
    n=int (input())
    sum=sum+n 
    total=total*n
    if not(sum<n and total<(n*n)):
        break