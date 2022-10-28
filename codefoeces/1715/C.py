import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os
# sys.setrecursionlimit(10000)
def values(): return tuple(map(int, sys.stdin.readline().split()))
def inlst(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(sys.stdin.readline())
def inpstr(): return sys.stdin.readline().strip()
def words(): return [i for i in sys.stdin.readline().split()]
def chars(): return list(sys.stdin.readline().strip())
def solve():
    n,m=values()
    l=inlst()
    s=set()
    tmp=l[0]
    tot=0
    for i in range(1,n):
        if l[i]!=tmp:
            s.add(i)
            tot += (i) * (n - (i))
        tmp=l[i]

    tot+=n*(n+1)//2

    for i in range(m):
        ind,x=values()
        if ind in s :
            s.remove(ind)
            tot-=ind*(n-ind)
        h=ind-1
        if h in  s:
            s.remove(h)
            tot -= h * (n - h)
        if ind<n and  x!=l[ind]:
            s.add(ind)
            tot+=ind*(n-ind)
        if ind>1 and x!=l[ind-2]:
            s.add(ind-1)
            tot+=(ind-1)*(n-(ind-1))
        l[ind-1]=x
        print(tot)

if __name__ == "__main__":
    # sys.stdin = open('/home/mohamed/Documents/w.txt', 'r')
    # for i in range(inp()):
        solve()