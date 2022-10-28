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
     r1,r2=values()
     c1,c2=values()
     d1,d2=values()
     s=set(i for i in range(1,10))
     x=(r1+c1-d2)/(2)
     if x==int(x):x=int(x)
     else:print(-1) ;return 0
     y=r1-x
     z=c1-x
     m=d1-x
     if x in s and y in s and z in s and m in s and len(set([x,y,z,m]))==4:
         if z+m==r2 and y+m==c2 and y+z==d2:
             print(x,y)
             print(z,m)
             return
     

     print(-1)


if __name__ == "__main__":
    # sys.stdin = open('/home/mohamed/Documents/w.txt','r')
    # for i in range(inp()):
        solve()