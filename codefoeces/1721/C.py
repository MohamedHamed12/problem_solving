import collections
import heapq
import sys
import math
import itertools
from bisect import bisect_left ,bisect_right
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
    n = inp()
    a=inlsts()
    b=inlsts()
    mn=[-1]*n
    mx=[-1]*n
    mx[-1]=b[-1]-a[-1]
    mn[-1]=(b[bisect_left(b,a[-1])]-a[-1])

    for i in range(n-2,-1,-1):
        if a[i+1]<=b[i]:
            mx[i]=mx[i+1]+ a[i+1]-a[i]
        else:mx[i]=b[i]-a[i]
        mn[i]=b[bisect_left(b,a[i])]-a[i]
    print(*mn)
    print(*mx)
if __name__ == "__main__":
    for i in range(inp()):
        solve()