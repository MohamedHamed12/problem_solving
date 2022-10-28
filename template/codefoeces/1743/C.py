import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os
######################################################################################
#--------------------------------------funs here-------------------------------------#
######################################################################################
def values(): return tuple(map(int, sys.stdin.readline().split()))
def inlsts(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(sys.stdin.readline())
def instr(): return sys.stdin.readline().strip()
def words(): return [i for i in sys.stdin.readline().strip().split()]
def chars(): return [i for i in sys.stdin.readline().strip()]
######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################
def solve():
    n = inp()
    s=list(instr())
    l=values()
    cost=[[0,0] for i in range(n)] 
    if s[0]=='1':  cost[0]=[l[0],-float('inf')]
    for i in range(1,n):
        if s[i]=='1':
            cost[i][0]=l[i]+max(cost[i-1])
            cost[i][1]=l[i-1]+cost[i-1][1]
        if s[i]=='0':
            cost[i][0]=max(cost[i-1])
            cost[i][1]=max(cost[i-1])
    print(max(cost[-1]))
            
        
    
if __name__ == "__main__":
    for i in range(inp()):
        solve()