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
    l=inlsts()
   
    if n==1:print(0);return 
    print(n-1)
    if (l[-1]+l[0])%2==0:
        l[0]=l[-1]
    else:l[-1]=l[0]
    print(1,n)
    val=l[-1]
    for i in range(1,n-1):
        if (l[i]+val)%2==0:print(i+1,n)
            
        else:print(1,i+1)
    
   


if __name__ == "__main__":
    for i in range(inp()):
        solve()