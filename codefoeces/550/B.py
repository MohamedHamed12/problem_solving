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
    n,low,high,diff=values()
    l=sorted(inlsts())
    tot=0
    for mask in range(1<<n):
        temsum=0
        mn=float('inf')
        mx=0
        b=True
        for j in range(n):
            if mask& (1<<j):
                mn=min(l[j],mn)
                mx=max(l[j],mx)
                temsum+=l[j]
            
              
            # if mx-mn>diff:b=False;break
            # if temsum>high:b=False; break
        if temsum<=high and   temsum>=low and mx-mn>=diff  :tot+=1

    return tot


if __name__ == "__main__":
        print(solve())