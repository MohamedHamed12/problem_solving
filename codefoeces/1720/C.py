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
    a, b = values()
    l=[]
   
    bb=False
    tot = 0
    for i in range(a):
        m = input()
        tot += m.count('1')
        l.append(m)
    for i in range(a):
        for j in range(b):
            if j<b-1 and l[i][j]=='0' and l[i][j+1]=='0':return tot
            if i<a-1 and l[i][j]=='0' and l[i+1][j]=='0':return tot
            if j<b-1 and  i<a-1 and  l[i][j]=='0' and l[i+1][j+1]=='0':return tot
            if j>0 and i<a-1 and l[i][j]=='0' and l[i+1][j-1]=='0':return tot
            elif  not bb and '0' in l[i] :bb=True
   

    if bb: return tot-1
    return tot-2
    


if __name__ == "__main__":
    for i in range(inp()):

        print(solve())