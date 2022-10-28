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
def inlsts(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(input())
def inps(): return int(sys.stdin.readline())
def instr(): return input()
def stlst(): return [i for i in input().split()]


######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################

def solve():
    n,m,x,z,y,p=value()
    x,y,z=x%4,y%4,z%2
    m0,n0=m,n
    for i in range(p):
        m,n=m0,n0
        xx,yy=value()
        for i in range(x):
            xx,yy=yy,n-xx+1
            n,m=m,n
        if z==1:
            yy=m-yy+1
        for i in range(y):
            xx,yy=m+1-yy,xx
            n,m=m,n
        print(xx,yy)



if __name__ == "__main__":
        solve()