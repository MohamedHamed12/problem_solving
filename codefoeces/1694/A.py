# from ntpath import join
from sys import stdin
# def solve(n,l):
#     pass

for i in range(int(input())):
  

    a,b=(map(int,stdin.readline().split()))
    l=[]
    while a>0 and  b>0:
        if a<b:
            l.append('1')
            l.append('0')
            a-=1;b-=1
        else:
             l.append('0')
             l.append('1')
             a-=1;b-=1
    while a>0:
         l.append('0')
         a-=1
    while b>0:
         l.append('1')
         b-=1
    print("".join(l))