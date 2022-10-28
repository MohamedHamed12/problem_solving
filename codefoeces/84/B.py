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
def inlsts(): return [int(i) for i in  sys.stdin.readline().split()]
def inp(): return int(input())
def inps(): return int(sys.stdin.readline())
def instr(): return input()
def stlst(): return [i for i in input().split()]
    
 
######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################
def cnt(n):
    return n*(1+n)//2
def solve():
    n=inp()
    l=inlst()
    tot=0
    for i , j in itertools.groupby(l):
        m=len(list(j))
        tot+=m+cnt(m-1)

    print(tot) 


 
solve()


# n = int(input())
# a = list(input().split())
 
# x = 0
# c = 0
# i = 0


# while i < n:
#     if i + x < n and a[i] == a[i + x]:
#         x += 1
#     else:
#         c += int((x * (x + 1)) / 2)
#         i += x
#         x = 0
 
# print(c)