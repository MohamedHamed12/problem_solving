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
    tot=0
    def check(p): 
        # nonlocal x1,y1
        a,b,c=p
        if a*x1+b*y1+c>0 and a*x2+b*y2+c<0:return True
        elif a*x1+b*y1+c<0 and a*x2+b*y2+c>0:return True
        else:return False

    for i in range(len(l)):
        if check(l[i]):tot+=1
    print(tot)
x1,y1=value()
x2,y2=value()
l=[]
for i in range(inp()):
    l.append(value())
solve()