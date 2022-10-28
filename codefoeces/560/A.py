import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os

# sys.setrecursionlimit(10000)

def values(): return tuple(map(int, sys.stdin.readline().split()))
def inlst(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(sys.stdin.readline())
def inpstr(): return sys.stdin.readline().strip()
def words(): return [i for i in sys.stdin.readline().split()]
def chars(): return list(sys.stdin.readline().strip())
def solve():
    n=inp()
    s=values()
    if 1 in s:print(-1)
    else:print(1)


if __name__ == "__main__":
    # sys.stdin = open('/home/mohamed/Documents/w.txt','r')
    # for i in range(inp()):
        solve()