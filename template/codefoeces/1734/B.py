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
    l=[]
    for i in range(n):
        s=''
        if  i<=1:
            s+=(i+1)*'1 '
        else:
            s+='1 '
            s+=(i-1)*'0 '
            s+='1 '

        l.append(s)
    for i in l:print(i)


if __name__ == "__main__":
    for i in range(inp()):
        solve()