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
    n,o,w=values()
    l=[]
    tem=0
    if w == 0 and o > 0:
        if o == n-1:
            print(-1)
            return
        print(1, end = " ")
        n-=1
        
    
    
    for i in range(1+w):
        l.append(tem+1)
        tem+=tem+1
    
    for i in range(o):
        # l.append(2**w + i + 1)
        l.append(l[-1]+1)
    for i in range(n-o-w-1):
            l.append(1);tem+=1

        # tem+=l[-1]
    print(*l)


 
solve()
# import sys


# n, a, b = input().split()
# n = int(n)
# a = int(a)
# b = int(b)
# if b == 0 and a > 0:
#     if a == n-1:
#         print(-1)
#         sys.exit()
#     print(1, end = " ")
#     n-=1
# for i in range(b+1) :
#     print(2**i, end = " ")
# for i in range(a) :
#     print(2**b + i + 1, end = " ")
# for i in range(n - a- b-1) :
#     print(1, end = " ")