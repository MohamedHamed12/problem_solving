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
def factors(n):
    res = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            res.append(i)
            if i != n//i:
                res.append(n//i)
    return res
 
def solve():
    a,b,c,d=values()
    l1=factors(a)
    l2=factors(b)
    for i in l1:
        for j in l2:    
            v1=i*j
            v2=a*b//v1
            x=(c//v1)*v1
            y=(d//v2)*v2
            if x>a and y>b :
                print(x,y);return 
    print(-1,-1)


if __name__ == "__main__":
    for i in range(inp()):
        solve()