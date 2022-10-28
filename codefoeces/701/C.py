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
def inst(): return input()
def stlst(): return [i for i in input().split()]
    
 
######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################
  
def solve():

 n=inp()
 st=inst()
 ln=len(set(list(st)))
#  tot=n
 c=collections.Counter(st[:ln])
 h=ln
 while len(c)!=ln:
        
        c[st[h]]+=1
        h+=1
        
 tot=sum(c.values())
 h=tot
 ind=0

 for i in range(h,n+1):
            
    while c[st[ind]]>1:
                
        c[st[ind]]-=1
        ind+=1
        tot=min(tot,sum(c.values()))
    if i<n:c[st[i]]+=1

#  while c[st[ind]]>1:
                
#             c[st[ind]]-=1
#             ind+=1
#             tot=min(tot,sum(c.values()))
 print(tot)
        #  return 

# while c[st[ind]]>1:
                
#        c[st[ind]]-=1
#        ind+=1
#        tot=min(tot,sum(c.values()))
#        c[st[i]]+=1   
#  print(tot)


 

solve()