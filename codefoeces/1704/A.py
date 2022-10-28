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
def inlsts(): return [int(
    i) for i in  sys.stdin.readline().split()]
def inp(): return int(input())
def inps(): return int(sys.stdin.readline())
def instr(): return input()
def stlst(): return [i for i in input().split()]
    
 
######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################
  
def solve():
   a,b=values()
   s1=list(input()) 
   s2=list(input()) 
#    print(s2,s1[a-b:])
#    print(s2[1:],s1[(a-b)+1:] )
   if s2==s1[a-b:]:return "YES"
   elif s2[1:]==s1[(a-b)+1:] and s2[0] in s1[:(a-b)+1]  :return "YES"
   else:return "NO" 
        


 
for i in range(inp()):
    print(solve())