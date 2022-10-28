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
def values(): return list(map(int, sys.stdin.readline().split()))
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
    l=sorted(values())
    dp=[0]*(n+1)
    for i in range(n):dp[i+1]=dp[i]+l[i]
    tot=0
    for i in range(n):
        tot+=abs((i*l[i])-dp[i])
    a=dp[-1]+2*tot
    b=n
    c=math.gcd(a,b)
    print(a//c,b//c)
        


if __name__ == "__main__":
    # for i in range(inp()):
        solve()