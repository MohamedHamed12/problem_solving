import collections
import heapq
from operator import le
import re
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
def solve(n,m):
    if n==1:return 0
    tem=[1]*n
    h=0
    def do_remove(h,l): 
          for i in range(n):
                del l[i][h]
    def check(n):
        nonlocal tem,h
        t=[0]*n
        for i in range(1,n):
            
            if tem[i]==1:
                if  l[i][h]==l[i-1][h]:t[i]=1
                if l[i][h]<l[i-1][h]:
                    do_remove(h,l)
                    # if l:
                    #     # check(n)
                    return

        tem=t[:]
        h+=1
    while l and 1 in tem and h<len(l[0]):
        
      check(n)
    return (m-len(l[0]))
   
            
    
n,m=value()

l=[list(instr()) for i in range(n)]
print(solve(n,m))