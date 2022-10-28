import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os
from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10**7)
import threading
threading.stack_size(2**26)
######################################################################################
#--------------------------------------funs here-------------------------------------#
######################################################################################
def values(): return tuple(map(int, sys.stdin.readline().split()))
def inlsts(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(sys.stdin.readline().strip())
def instr(): return sys.stdin.readline().strip()
def words(): return [i for i in sys.stdin.readline().strip().split()]
def chars(): return [i for i in sys.stdin.readline().strip()]
######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################
def solve():
    n = inp()
    d=collections.defaultdict(list)
    for i in range(n-1):
        a,b=values()
        d[a].append(b)
        d[b].append(a)
    def dfs(u,p):
        tot=0
        for v in d[u]:
            if v!=p:tot+=dfs(v,u)+1
        if tot==0:return 0
        if u==1:return tot/(len(d[u]))
        else :return tot/(len(d[u])-1)
    print(dfs(1,0))



def mean():
        solve()


threading.Thread(target=solve).start()