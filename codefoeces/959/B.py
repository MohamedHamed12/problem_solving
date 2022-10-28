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
def valid(i,j,n,m):
        if i<n and i>=0 and j>=0 and j< m :return True #and l[i][j]==1 and visit[i][j]
        return  False
def sumn(i,n):
    return (n-i)*(i+n)/2
def sqfun(a,b,c):
    return (-b+math.sqrt(b*b-4*a*c))/2*a
######################################################################################
#--------------------------------------vars-----------------------------------------#
######################################################################################
# index=[[1,0],[0,1],[-1,0],[0,-1]]

######################################################################################
#--------------------------------------Input-----------------------------------------#
######################################################################################


def value(): return tuple(map(int, input().split()))
def values(): return tuple(map(int, sys.stdin.readline().split()))
def inlst(): return 
def inlsts(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(input())
def inps(): return int(sys.stdin.readline())
def instr(): return input()
def stlst(): return [i for i in input().split()]
def words(): return [i for i in input().split()]


######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################
def f():
    dd={}
    i=0
    for w in sys.stdin.readline().split():
            dd[w]=i
            i+=1
            wd.append(w)
    return dd
def kin():
    
    l=[int(i)-1 for i in input().split()]
    nn=l.pop(0)
    l=sorted(l)
    mn=cost[l[0]]
    for i in l:
        mn=min(mn,cost[i])
        d[wd[i]]=l[0]
    cost[l[0]]=mn
def solve():
    global wd ,d,cost
    wd=[]
    n,k,m=values()
    d=f()
    cost=inlsts()
    for i in range(k):
        kin()
    tot=0
    r=words()
    for i in r:tot+=cost[d[i]]
    return tot





if __name__ == "__main__":
    # for i in range(inp()):
       print(solve())