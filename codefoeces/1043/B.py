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
    tot=[]
    k=[l[0]]
    for i in range(1,n):
        k.append(l[i]-l[i-1])
    for i in range(1,n+1):
        if k[i:]==k[:-i]:tot.append(i )

    print(len(tot))
    print(*tot)
if __name__ == "__main__":
        solve()