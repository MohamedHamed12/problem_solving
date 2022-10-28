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
  
def solve(n,t,l):
    ss=sum(l)

    # tot=[]
    if n==1:l[0]-=1
    else:
        for i in range(n):
            rem=ss-l[i]
            a1=max(1,t-rem)
            a2=min(t-(n-1),l[i])
            l[i]-=a2-a1+1
        
        
     
    print(*l)
    l.clear()



n,s=values()
l=inlsts()
solve(n,s,l)