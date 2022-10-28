import collections
from email.policy import default
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
       l=inlsts()
       dp=l[0]
       s=sum(l)
       if s%3!=0: return 0
       s1=s//3
       h=0;tot=0
       for i in range(1,n):
             if dp==2*s1 and i!=1:tot+=h
             if dp==s1:h+=1
           
             dp=dp+l[i]
           
       return tot
           
            
            
            

 
print(solve())