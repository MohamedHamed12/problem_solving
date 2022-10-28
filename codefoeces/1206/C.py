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
     l=[]
     tem=[]
     t1=1;t2=2
     if n%2==0:
            print("NO")
            return 
     for i in range(n):
            if i%2==0:
                l.append(t1)
                tem.append(t2)
            else:
                l.append(t2)
                tem.append(t1)
            t1+=2
            t2+=2
     print("YES")
     print(*(l+tem))
            
        
            

 
solve()