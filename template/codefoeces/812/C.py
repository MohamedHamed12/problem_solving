
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
def addation(n):
    return (n*(n*n+n)//2)
def solve():
    n,k=value()
    lst=inlst()
    
    nums=0
    m=0
    lft=0; r=n
    while r-lft>1:
        tot=0
        m=(lft+r)//2
        heap=[]
        for i in range(n):
            heapq.heappush(heap,(lst[i]+(i+1)*m))
        for i in range(m):
            tot+=heapq.heappop(heap)
        if tot<=k:lft=m
        else:r=m
    res=0
    res2=0
    heap=[]
    for i in range(n):
            heapq.heappush(heap,lst[i]+((i+1)*lft))
    for i in range(lft):
            res+=heapq.heappop(heap)
    heap=[]
    for i in range(n):
            heapq.heappush(heap,lst[i]+((i+1)*r))
    for i in range(r):
            res2+=heapq.heappop(heap)
    if res2<=k:
      print(r,res2)
    else:
        print(lft,res)

solve()