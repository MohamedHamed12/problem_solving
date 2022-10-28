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
    l=[ i for i in range(1,n)]
    l.insert(1,n)
    print (*l)



if __name__ == "__main__":
    for i in range(inp()):
        solve()