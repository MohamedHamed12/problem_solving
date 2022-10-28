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
    a,b,c,d=values()
    ab=a*b
    for x in range(a+1,c+1):
        s=ab//math.gcd(x,ab)
        y=(d//s)*s
        if y>b:
            print(x,y);return
    print(-1,-1)

 


if __name__ == "__main__":
    for i in range(inp()):
        solve()