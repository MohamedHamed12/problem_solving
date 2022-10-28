from collections import deque
from  sys import stdin
def test(problem):
    pass
def solve(l,n):
    tem=deque()
    while  len(tem)<3:
      tem.append(n)
      n=l[n-1]
      if n==0:
            if len(tem)==3:break
            print("NO")
            return
    print("YES")
    return 
    

n=int(input())
for i in range(n):
   n=int(input())
   l=list(int(i) for i in stdin.readline().split())
   solve(l,n)