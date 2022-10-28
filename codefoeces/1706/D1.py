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
    n,k=value()
    arr=inlsts()
    mn=min(arr)
    ans=float('inf')
    if k>=max(arr):return 0

    for o in range(1,(mn+1)):
        temx=0;temn=float('inf')
        for i in range(n):
            tem=min(arr[i]//o,k)
            temx=max(temx,arr[i]//tem)
            temn=min(temn,arr[i]//tem)
        ans= min(ans,temx-temn)


    return ans
if __name__ == "__main__":
    for i in range(inp()):
        print(solve())