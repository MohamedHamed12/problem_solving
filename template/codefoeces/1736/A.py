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
    ll=values()
    tot=0
    for i in range(n):
        if l[i]!=ll[i]:tot+=1
    a=l.count(1)
    b=ll.count(1)
    a=abs(a-b)+1
    print(min(a,tot))

if __name__ == "__main__":
    for i in range(inp()):
        solve()