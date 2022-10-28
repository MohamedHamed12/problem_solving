# 1/2  2/3  4/5
from sys import stdin
import math


def ssolve():
    a, b = (map(int, stdin.readline().split()))
    l=[0,0,0]
    while a % 5 == 0:
        a = a//5
        l[0]+=1
        
    while a % 3 == 0:
        a=a//3
        l[1]+=1
    while a % 2 == 0:
        a=a//2
        l[2]+=1
   



    while b % 5 == 0:
        b = b//5
        l[0]-=1
    while b % 3 == 0:
        b=b//3
        l[1]-=1
    while b % 2 == 0:
        b=b//2
        l[2]-=1
    if b==a:
        
        tot=0
        for i in l:
            tot+=abs(i)
        return tot
    else:
        return -1
print(ssolve())