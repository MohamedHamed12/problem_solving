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
    l=values() 
    s=set()
    ss=[]
    for i in range(n-1,-1,-1):
        if l[i] not in s:s.add(l[i]);ss.append((l[i],i+1))
    f=-1
    for i in range(len(ss)):
        for j in range(i,len(ss)):
            sm=ss[i][1]+ss[j][1]
            if sm>f:
                if math.gcd(ss[i][0],ss[j][0])==1:
                    f=sm;break

        
      
    print(f)

if __name__ == "__main__":
    for i in range(inp()):
        solve()