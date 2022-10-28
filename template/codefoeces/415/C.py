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
  
def solve():
    nn,k=value()
    if nn%2==1 :
        n=nn-1 
    else :
        n=nn
    if nn==1 :
            if k==0:print(1)
            else:print(-1)
            return
    if  k<n//2:
            print(-1)
            return 
    gfirst=k-(-1+(n//2))
    l=[]
    l.append(gfirst)
    l.append((gfirst*2))
    for i in range(2,nn):
            l.append((l[-1]+1))
    print(*l)


 
solve()