import re
from  sys import stdin
def test(problem):
    pass
def solve(n,x,l):
    l=sorted(l)
    l1=l[:n]
    l2=l[n:]
    for i in range(n):
        if l2[i]-l1[i]<x:return "NO"

    return "YES"


for i in range(int(input())):
    n,x=list(int(i) for i in stdin.readline().split())
    l=list(int(i) for i in stdin.readline().split())
    print(solve(n,x,l))