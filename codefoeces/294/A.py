import collections
import heapq
from re import X
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
    l=inlsts()
    m=inp()
    for i in range(m):
        x,y=values()
        x-=1
        if x-1>=0: l[x-1]+=y-1
        if x+1<n: l[x+1]+=l[x]-y
        l[x]=0
    for i in l: print (i)
       



if __name__ == "__main__":
    # for i in range(inp()):
        solve()