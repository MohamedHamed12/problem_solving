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
    
sys.setrecursionlimit(10**9)
######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################
class sol:
    def __init__(self,dd,ll,kk,n):
         self.d=dd
         self.l=ll
         self.k=kk
         self.visit=[True]*(n+1)
         self.tot=0
    def dfs(self,r,pp):
        q=[(r,pp)]
        while q:
            root,p=q.pop()

            self.visit[root]=False
            if p>self.k:continue
                
            if self.l[root-1]==1:
                p+=self.l[root-1]
            else:p=0
            
            m=True
            for i in self.d[root]:
                if self.visit[i]:
                   q.append((i,p))
                   m=False
            if m:
                if p<=self.k:self.tot+=1
   
        
        



def solve():
    n,k=value()
    l=inlsts()
    d=collections.defaultdict(set)
    for i in range(n-1):
        u,v=value()
        d[u].add(v)
        d[v].add(u)
    s=sol(d,l,k,n)
    s.dfs(1,0)
    print(s.tot)
solve()


 # def dfs(self,root,p):
    #     self.visit[root]=False
    #     if p>self.k:return
              
    #     if self.l[root-1]==1:
    #         p+=self.l[root-1]
    #     else:p=0
        
    #     m=True
    #     for i in self.d[root]:
    #          if self.visit[i]:
    #            self.dfs(i,p)
    #            m=False
    #     if m:
    #         if p<=self.k:self.tot+=1