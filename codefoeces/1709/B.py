from collections import deque
from  sys import stdin
def test(problem):
    pass
def solve(n,b,l):
    t1=deque()
    t2=deque()
    t1.append(0)
    t2.append(0)
    for i in range(1,n):
            t1.append(max(l[i-1]-l[i],0)+t1[-1])
    for i in range(n-1,0,-1):
           t2.insert(0,max(l[i]-l[i-1],0)+t2[0])
   
    for i in range(b):
        k,h=list(int(i) for i in stdin.readline().split())
        if k<h:print(t1[h-1]-t1[k-1])
        else:print(t2[h-1]-t2[k-1])

n,b=list(int(i) for i in stdin.readline().split())
l=list(int(i) for i in stdin.readline().split())

solve(n,b,l)

  
# t=tuple()
# t.__add__(1)
# print(t)