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


def solve():
      m,n=values()
      dp=[0]*m
      for i in range(n):
          l = values()
          dp[l.index(max(l))]+=1

      return dp.index(max(dp))+1





if __name__ == "__main__":
#     # sys.stdin = open('/home/mohamed/Documents/w.txt','r')
#     for i in range(inp()):
       print( solve())



'''
3 3
1 2 3
2 3 1
1 2 1
'''