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
    mn=min(l)
    idx=[]
    for i in range(n):
        if l[i]==mn:idx.append(i)
    mx=n-idx[-1]-1+idx[0]
    for i in range(1,len(idx)):
        mx=max(mx,idx[i]-idx[i-1]-1)
    print(mn*n+mx)
        

if __name__ == "__main__":
        solve()