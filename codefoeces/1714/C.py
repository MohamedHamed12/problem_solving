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
    n=inp()
    
    if n<10:
        print(n)
        return
    else:
        l=[9]
        n-=9
        while n>0:
            if n<10 and n not in l:
                l.append(n)
                break
            n-=l[-1]-1
            l.append(l[-1]-1)
    l=l[::-1]
    for i in l:print(i,end="")
    print()

 
for i in range(inp()):
    solve()