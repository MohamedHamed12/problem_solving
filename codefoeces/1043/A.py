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
    l=inlst()
    mx=max(l)
    tot=0
    s=sum(l)
    for i in range(n):
        tot+=mx-l[i]
    if tot>s:return mx
    tem=math.ceil((s-(tot-1))/n)
    return mx+tem


if __name__ == "__main__":
       print(solve())