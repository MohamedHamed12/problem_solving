import collections
import heapq
from re import T
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
  
# def solve():
#     n,x=values()
#     l=inlsts()
#     m=min(l)
#     indmin=l.index(m)
#     b=False
#     for i in range(x-1,-1,-1):
#         if l[i]==m:indmin=i
#         b=True
#         break
#     if not b:
#         for i in range(n-1,x-1,-1):
#             if l[i]==m:indmin=i
#             break
    
#     if len(set(l))==1:
#         indmin=x-1
   
#     if x-1>=indmin: 
#         tot=0
#         for i in range(n):
            
#             if i>indmin and i<x:l[i]-=m+1;tot+=m+1
#             else :l[i]-=m;tot+=m
#         l[indmin]=tot
#     else:
#         tot=0
#         for i in range(n):
            
#             if i>=x and i<=indmin:l[i]-=m;tot+=m
#             else :l[i]-=m+1;tot+=m+1
#         l[indmin]=tot
#     print(*l)


 
# solve()



def solve():
    n,x=values()
    l=inlsts()
    m=min(l)
    tem=m*n
    for i  in range(n):l[i]-=m
    x-=1
    while True:
        if  l[x]==0:
            break

        l[x]-=1
        tem+=1
        x-=1
        if x==-1:x=n-1


    l[x]=tem

        
    print(*l)


 
solve()