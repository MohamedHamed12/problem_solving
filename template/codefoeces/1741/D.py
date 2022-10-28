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
    l=values()
    x=1; ans =0
    while x<n:
        for i in range(0,n,2*x):
            if abs( l[i] -l[i+x])!=x:ans=-1;break
            if l[i] >l[i+x]:
                l[i] ,l[x+i]=l[x+i] ,l[i];ans+=1
        x*=2
        if ans ==-1:break
    print(ans)


if __name__ == "__main__":
    for i in range(inp()):
        solve()