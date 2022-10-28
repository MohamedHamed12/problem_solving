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
    a25=0
    a50=0
    a100=0
    for i in range(n):
        if l[i]==25:a25+=1
        if l[i]==50:
            if a25>0:a25-=1;a50+=1
            else:return "NO"
        if l[i]==100:
            if a50>0 and a25>0:a50-=1;a25-=1
            elif a25>2:a25-=3
            else:return "NO"
    return "YES"

if __name__ == "__main__":
    # for i in range(inp()):
        print(solve())