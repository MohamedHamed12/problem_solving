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
def values(): return sys.stdin.readline().split()
def inlsts(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(sys.stdin.readline())
def instr(): return sys.stdin.readline().strip()
def words(): return [i for i in sys.stdin.readline().strip().split()]
def chars(): return [i for i in sys.stdin.readline().strip()]
######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################
def solve():
    n ,r=values();n=int(n)
    s=instr()
    mx=0
    tmp=-float('inf')
    for i in range(2*n):
        if s[i%n]=='g':
            mx=max(mx,tmp)
            tmp=-float('inf')
        elif s[i%n]==r:tmp=max(tmp+1,1)
        else:
            tmp+=1
    return mx
    



if __name__ == "__main__":
    for i in range(inp()):
        print(solve())