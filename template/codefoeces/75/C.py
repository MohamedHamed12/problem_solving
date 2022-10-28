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
    l=[1]
    a,b=values()
    if a<b :a,b=b,a
    m=int(math.sqrt(b))+1
    for i in range(2,m):
        if a%i==0 and b%i==0 :
            l.append(i)
        if i!=b//i and b%i==0 and a%(b//i)==0:
              l.append(b//i)
    # print(l)
    if a%b==0:l.append(b)
    l=sorted(l)
    n=inp()
    for i in range(n):
        lft,r=values()
        ind=bisect.bisect_right(l,r)-1
        if ind >=bisect.bisect_left(l,lft):
            print(l[ind])
            
        else:
            print(-1)

 

solve()
# l=[]
# a,b=9,27
# for i in range(3):
#     l.append(math.gcd(27))