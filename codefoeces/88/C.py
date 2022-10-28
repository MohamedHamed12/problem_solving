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
  
def solve(a,b):
    h='Dasha'
    k='Masha'
    e='Equal'
    m=(a*b)//(math.gcd(a,b))
    x=(m//a)-1
    y=(m//b)-1
    if x>y+1:
        print(h)
    elif y>x+1:
        print(k)
    else:
        print(e)
  
a,b=values()
solve(a,b)