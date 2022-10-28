import code
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
    n,t,c=values()
    l=inlsts()
    tot=0
    tem=0
    for i in range(n):
        if l[i]<=t:tem+=1
        else:
            tot+=max(0,tem-c+1)
            tem=0
    tot+=max(0,tem-c+1)
    # i=0
    # while i+c<=n:
    #     b=True
    #     m=i+c
    #     for j in range(i,m):
    #         if l[j]>t:
    #             i=j+1
    #             b=False
    #     if b:
    #         tot+=1
    #         i+=1
    print(tot) 

if __name__ == "__main__":
        solve()