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
    n=inp()
    if n%2 == 0:print('Mahmoud')
    else:print('Ehab')


if __name__ == "__main__":
    # for i in range(inp()):
        solve()