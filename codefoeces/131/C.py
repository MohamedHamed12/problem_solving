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
  
def solve(a,b,t):
    tot=0
    for i in range(4,a+1):
        if t-i < 1:break
    		
        tot+=math.comb(a,i)*math.comb(b,t-i)
    print(tot)

    # m=math.comb(a+b,t)-math.comb(a,t) -math.comb(b,t)
    # -math.comb(a,1)*math.comb(b,t-1)
    # -math.comb(a,2)*math.comb(b,t-2)
    # -math.comb(a,3)*math.comb(b,t-3)
    # print(m)
   


a,b,t=values()
solve(a,b,t)

# n=math.comb(2,1)
# print(n)