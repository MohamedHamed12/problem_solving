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
    nums=list(input())
    mn=float('inf')
    # ind=num.index(mn)
    for j in range(n):
        num=nums.copy()
        num=num[j:]+num[:j]
        for i  in range(n):
            num[i]=str((int(num[i])-int(nums[j])+10)%10)
        mn=min(mn,int("".join(num)))
    print(str(mn).zfill(n))




if __name__ == "__main__":
        solve()