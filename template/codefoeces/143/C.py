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
def get2(n):
    m = math.ceil(math.pow(n, 1 / 2))
    for i in range(m ,0,-1):
        if n % i == 0:
            return (i,n//i)
def get(n):
    l=[n,1,1]
    r=float('inf')
    m=math.ceil(math.pow(n,1/3))
    for i in range(m,0,-1):
        if n%i==0 :
            a,b=get2(n//i)
            l=[a,b,i]
            l=sorted(l)
            tmp=(l[-1]+2)*(l[-2]+2)*(l[0]+1)-n
            r=min(tmp,r)


    return r



def solve():
    m=inp()
    a=get(m)
    b=8*m+9
    print(a,b)


if __name__ == "__main__":
    # sys.stdin = open('/home/mohamed/Documents/w.txt','r')
    # for i in range(inp()):
        solve()