import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os
######################################################################################
#--------------------------------------Input-----------------------------------------#
######################################################################################


def value(): return tuple(map(int, input().split()))
def values(): return tuple(map(int, sys.stdin.readline().split()))
def inlst(): return [int(i) for i in input().split()]
def inlsts(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(input())
def inps(): return int(sys.stdin.readline())
def instr(): return input()
def stlst(): return [i for i in input().split()]


######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################

def solve():
    n = inp()
    l=inlsts()
    ind ,mx=0,float('inf')
    for i in range(1,n-1):
        tem=l.copy()
        tem.pop(i)
        temmx=0
        for j in range(1,n-1):
           temmx=max(temmx, tem[j]-tem[j-1])
        mx=min(mx ,temmx )
        # if mx <tem[j]-tem[j-1] :
        #   ind =i
    return mx


if __name__ == "__main__":
        print(solve())