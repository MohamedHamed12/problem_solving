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
    
    n=inp()
    d=values()
    t=values()
    mn,mx=float('inf'),-float('inf')
    for i in range(n):
        mn=min(mn,d[i]-t[i])
        mx=max(mx,d[i]+t[i])
    print((mn+mx)/2)


if __name__ == "__main__":
    for i in range(inp()):
        solve()
0