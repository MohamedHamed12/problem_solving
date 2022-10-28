import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os
from webbrowser import get

 
def value(): return tuple(map(int, input().split()))
def values(): return tuple(map(int, sys.stdin.readline().split()))
def inlst(): return [int(i) for i in input().split()]
def inlsts(): return [int(i) for i in  sys.stdin.readline().split()]
def inp(): return int(input())
def inps(): return int(sys.stdin.readline())
def instr(): return input()
def stlst(): return [i for i in input().split()]
    
 
def gettime(t1,t2):
    h1,m1=t1
    h2,m2=t2
    if m1<m2:
        m1+=60
        h1-=1
    return (abs(h1-h2),abs(m1-m2))

def solve(n ,h1,m1):
  
   t=(h1,m1)
   l=[]
   for i in range(n):
        l.append(value())
   l=sorted(l)
   ind=bisect.bisect_left(l,t)
   if ind==n:
        k=gettime(t,l[0])
        print(*gettime((24,0),k))

   else:
        print(*gettime(l[ind],t))


        

n=int(input())
for i in range(n):
    x,y,z=values()
    solve(x,y,z)