import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os

# sys.setrecursionlimit(10000)

def values(): return tuple(int(i) for i in sys.stdin.readline().split())
def inlst(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(sys.stdin.readline())
def inpstr(): return sys.stdin.readline().strip()
def words(): return [i for i in sys.stdin.readline().split()]
def chars(): return list(sys.stdin.readline().strip())

def get(n):
    x=2*n-1
    return n*(1+x)//2
def solve():
        a1,a2,a3,a4,a5,a6=values()
        l=a6+a2+a1
        return get(l)-get(a2)-get(a4)-get(a6)




if __name__ == "__main__":
#     # sys.stdin = open('/home/mohamed/Documents/w.txt','r')
#     for i in range(inp()):
       print( solve())