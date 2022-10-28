from collections import deque
from sys import stdin

def solve(n,l):
    s=0
    for i in range(n):
    
        s+=l[i]
        if s<0:
            return "No"
        if s==0 and i <n-1:
            for i in range(i+1,n):
                if l[i]!=0:
                   return "No"
            return  "YES"
            
    if s==0:
        return "Yes"
    else:
        return "NO"

for i in range(int(stdin.readline())):
    n=int(stdin.readline())
    # a,b=map(int,input().split())
    # d=deque()
    d=[]
    for i in stdin.readline().split():
        d.append(int(i))

    # l=list(int i )
    print(solve(n,d))