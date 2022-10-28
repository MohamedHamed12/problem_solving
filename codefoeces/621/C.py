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
    n,p=values()
    l=[]
    for i in range(n):
        a,b=sorted(values())
        ln=b-a+1
        d=b//p -(a-1)//p
        l.append((ln,d))
    l.append(l[0])
    ans=0
    for i in range(n):
        n1,a1=l[i]
        n2,a2=l[i+1]
        ans+=1-(n1-a1)*(n2-a2)/(n1*n2)
    print(ans*2000)


if __name__ == "__main__":
    # for i in range(inp()):
        solve()


# n, p = [int(x) for x in input().split()]
# Arr = []
 
# for i in range(n):
# 	tmp1, tmp2 = [int(x) for x in input().split()]
# 	cnt = tmp2 // p - (tmp1 - 1) // p
# 	Arr.append(cnt / (tmp2 - tmp1 + 1))
 
# Arr.append(Arr[0])
 
# ans = 0.0
 
# for i in range(n):
# 	p1 = Arr[i]
# 	p2 = Arr[i + 1]
# 	ans += p1 + p2 - p1 * p2
 
# print(ans * 2000)