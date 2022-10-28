import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os
######################################################################################
#--------------------------------------func-----------------------------------------#
######################################################################################

######################################################################################
#--------------------------------------vars-----------------------------------------#
######################################################################################
# index=[[1,0],[0,1],[-1,0],[0,-1]]

######################################################################################
#--------------------------------------Input-----------------------------------------#
######################################################################################


def value(): return tuple(map(int, input().split()))
def values(): return tuple(map(int, sys.stdin.readline().split()))
def inlst(): return [int(i) for i in input().split()]
def inlsts(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(input())
def inps(): return int(sys.stdin.readline())
def instr(): return input()
def stlst(): return [i for i in input().split()]


######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################


def solve():
    n,k=value()
    l=inlst()
   
    mx=max(l)
    ind =0
    d=collections.defaultdict(list)
    for i in range(1,n):
        if l[i] >l[ind]:
            ind=i
        if len(d[l[ind]])>1:
                    d[l[ind]][-1]+=1
        else:
                d[l[ind]].append(i)
        if l[i]==mx:break
    for i in range(k):
        a,b=values()
        a=l[a-1]
        if a==mx:
            if d[a][0]>b:print(0) 
            else:print(b-d[a][0]+1) 
            continue
        if  len(d[a])>0:
            if len(d[a])>1:
                if b<d[a][0]:
                    print(0) 
                elif b>d[a][1]:
                    print(d[a][1]-d[a][0]+1) 
                else:
                    print(b-d[a][0]+1) 
            
            else:
                if b>=d[a][0]:print(1)
                else :print(0)
                
        
        else:print(0) 
if __name__ == "__main__":
    for i in range(inp()):
        (solve())