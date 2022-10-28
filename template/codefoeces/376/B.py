from collections import defaultdict
from  sys import stdin
def test(problem):
    pass
def solve(problem):
    pass

    

d=defaultdict(int)
n,m=list(int(i) for i in stdin.readline().split())
for i in range(m):
    a,b,c=list(int(i) for i in stdin.readline().split())
    d[a]-=c
    d[b]+=c
tot=0
for i in d:
    if d[i]<0:
        tot+=abs(d[i])
print(tot)