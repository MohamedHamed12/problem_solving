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
    s=instr()
    d=collections.defaultdict(set)
    for i in range(n):
        d[s[i]].add(l[i])
    c=collections.Counter(l)
    cc=collections.Counter(s)
    for i in d:
        tmp=0
        for j in d[i]:
            tmp+=c[j]
        if tmp!=cc[i]:return "NO"
    return "YES"


if __name__ == "__main__":
    for i in range(inp()):
        print(solve())