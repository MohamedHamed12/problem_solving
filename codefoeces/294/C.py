
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
    n ,m=values()
    l=sorted(values())
    tmp=[]
    tmp.append(l[0]-1)
    for i in range(1,len(l)):
        tmp.append(l[i]-l[i-1]-1)
    tmp.append(n-l[-1])
    tot=1
    for i in range(1,m):
        if tmp[i]!=0:tot=(tot*(2**(tmp[i]-1)))
    sm=tmp[0]
    for i in range(1,len(tmp)):
        
        tot=(tot*math.comb(sm+tmp[i],sm))
        sm+=tmp[i]
    print(tot%mod)




if __name__ == "__main__":
    # for i in range(inp()):
        solve()
from math import *