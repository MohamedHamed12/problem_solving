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
def values(): return tuple(map(int, sys.stdin.readline().split()))
def inlsts(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(sys.stdin.readline())
def instr(): return sys.stdin.readline().strip()
def words(): return [i for i in sys.stdin.readline().strip().split()]
def chars(): return [i for i in sys.stdin.readline().strip()]
######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################
def solve():
    n = inp()
    t=[];w=[]
    for i in range(n):
        a,b=values()
        t.append(a);w.append(b)
    sm=sum(t)
    cnt=sum(w)
    dp=[-float('inf')]*(sm+1)
    dp[0]=0
    for i in range(n):
        for j in range(sm,t[i]-1,-1):
            dp[j]=max(dp[j],dp[j-t[i]]+w[i])
    for i in range(1,len(dp)):
        rem=cnt-dp[i]
        if  dp[i] >0 and rem<=i:print(i);break
         

if __name__ == "__main__":
    # for i in range(inp()):
        solve()


# t = [0]
# w = [0]
# n = int(input())
# for i in range(1, n+1):
#     a, b = map(int, input().split())
#     t.append(a)
#     w.append(b)

# sm=sum(t)
# cnt=sum(w)


# dp=[0]*(sm+1)
# dp[0]=0
# for i in range(1,n+1):
#         for j in range(sm,t[i]-1,-1):
#            dp[j]=max(dp[j],dp[j-t[i]]+w[i])

# for i in range(1,sm+1):
#     if dp[i]>0 and i>=cnt-dp[i]:
#         print(i,end='\n')
#         break
# print([(i,dp[i]) for i in range(len(dp))])


# memo = {}

# ans = 10**9

# def rec(hh, ww, i):
#     if i == n+1:
#         if ww <= hh:
#            return hh
#         else:return float('inf')
#     if (hh, ww, i) in memo:memo[(hh, ww, i)]
#     memo[(hh, ww, i)]=min(rec(hh+t[i], ww, i+1), rec(hh, ww+w[i], i+1))
#     return memo[(hh, ww, i)]


# print(rec(0, 0, 0))