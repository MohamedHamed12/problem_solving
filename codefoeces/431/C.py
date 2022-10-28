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
    mod=7+10**9
    n,k,d=values()
    dp={}
    def rec(sm,x): 
        if sm==n and x:return 1
        if sm>=n:return 0
        if (sm,x) in dp:return dp[(sm,x)]
        ans=0
        for i in range(1,k+1):
            ans=(ans%mod+rec(sm+i,x or i>=d)%mod)%mod
        dp[(sm,x)]=ans
        return ans
            
    print(rec(0,0))


if __name__ == "__main__":
    # for i in range(inp()):
        solve()