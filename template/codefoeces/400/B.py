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
    n,m=values()
    take=set()
    stop=set()
    b=True
    for i in range(n):
        s=instr()
        g=s.index("G");ss=s.index("S")
        if ss>g:
            take.add(ss-g)
            stop.add(m-g-1)
        else:b=False
    if not b:return -1
    mx=max(take)
    # for i in sorted(stop):
    #     if i<mx:take.add(i)
    #     else:break
    return len(take) 


if __name__ == "__main__":
        print(solve())