import math
t=int(input())
for i in range(t):
    n,s=map(int,input().split())
    if n==1:
        print(s)
    elif s==1 :
        print(0)
    else :
        if n%2==0:
           print(int (s/( (n/2)+1)))
        else:
           print(int (s/(int(n/2)+1)))