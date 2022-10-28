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
    nn=inp()
    n=nn
    if n<=2:
       m=int(math.sqrt(n))+1
    ind =2
    l=[]
    while ind <= math.sqrt(n):
        while n%ind == 0:
            n=n//ind
            l.append(ind)

        ind+=1
        if len(l) ==2 and l[0]*l[1]!=nn:
            print(1)
            print((l[0]*l[1]))
            return 
        if len(l) >2 :
            print(1)
            print((l[0]*l[1]))
            return 
        
    if len(set(l))==1:
      print(2)
    else:
        print(1)
        print(0)
        

 

solve()