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

    n = int(input())
    a = sorted(map(int, input().split()))
    ans = 0
    for i in range(n):
        l = 0; r = i 
        c = (i+2)//2
        chk = 0
        while l <= r:
            if a[r] <= c-l:
                r -= 1 ; l += 1
               
            else:
                chk = 1
                break
        if chk == 0:  ans = c
          
    print(ans)

if __name__ == "__main__":
    for i in range(inp()):
        solve()