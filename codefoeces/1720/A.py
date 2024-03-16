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


def valid(i, j, n, m):
    if i < n and i >= 0 and j >= 0 and j < m:
        return True  # and l[i][j]==1 and visit[i][j]
    return False


def sumn(i, n):
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
    a, b, c, d = values()

    if a*d == c*b :
        return 0
    if 0 in [a,b,c,d]: return 1
    tmp= (a*d)/(c*b)
    if tmp==int(tmp) and tmp!=1:return 1
    tmp= (c*b)/(a*d)
    if tmp==int(tmp) and  tmp!=1:return 1
    return 2
    


if __name__ == "__main__":
    for i in range(inp()):
        print(solve())