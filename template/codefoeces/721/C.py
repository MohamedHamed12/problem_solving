import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os
######################################################################################
#--------------------------------------funs here-------------------------------------#
######################################################################################
def values(): return (map(int, sys.stdin.readline().split()))
def inlsts(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(sys.stdin.readline())
def instr(): return sys.stdin.readline().strip()
def words(): return [i for i in sys.stdin.readline().strip().split()]
def chars(): return [i for i in sys.stdin.readline().strip()]
######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################
def solve():
    n,m,t=map(int, input().split())
    d=collections.defaultdict(list)
    
    for _ in range(m):
        a,b,c=values()
        d[a].append((b,c))
    dp=[[t+1]*(n+1) for _ in range(n+1) ]
    pre= [[0 for _ in range(n+1)] for _ in range(n + 1)]
    q=collections.deque()
    q.append( (1,1,0))
    dp[1][1] = 0
    pre[1][1] = 0  
    while q:
         tmpq=collections.deque()
    
         for root,num,rcost in  q:
            num+=1
            
            for v,w in d[root]:
                costw=rcost+w
                if costw<=t and costw<dp[v][num]:
                    dp[v][num]=costw
                    tmpq.append((v,num,costw))
                    pre[v][num]=root
         q=tmpq
        
    ans = max([i for i in range(n,-1,-1) if dp[n][i] <= t])
    root=n
    print(ans)
    tmp=[]
    while root:
        tmp.append(root)
        root=pre[root][ans]
        ans-=1
    print(' '.join(map(str, tmp[::-1])))
    # print(*tmp[::-1])




solve()