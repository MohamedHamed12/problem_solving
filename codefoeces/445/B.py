from collections import defaultdict
from  sys import stdin
import sys
def test(problem):
    pass
tot=1
def dfs(r):
    tot=1
    # nonlocal tot
    q=[r]
    while q:
        root=q.pop()
        visit[root-1]=False
        for item in d[root]:
            if visit[item-1] and item not in q :
                    q.append(item)
                    tot*=2
        visit[root-1]=False
    return tot
def solve():
    tot=1
    for i  in range(1,n+1):
        
        if visit[i-1] :
            tot*=dfs(i)
    
    print(tot)


n,b=list(int(i) for i in stdin.readline().split())
d=defaultdict(list)
visit=[True]*n

for i in range(b):
    u,v=map(int ,input().split())
    d[u].append(v)
    d[v].append(u)
# print("Yes") if solve() else print("No")
    
 
solve()