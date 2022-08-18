import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os

# sys.setrecursionlimit(10000)
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
# mod = 10 ** 9 + 7
######################################################################################
#--------------------------------------Input-----------------------------------------#
######################################################################################


def values(): return tuple(map(int, sys.stdin.readline().split()))
def inlst(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(sys.stdin.readline())
def inpstr(): return sys.stdin.readline().strip()
def words(): return [i for i in sys.stdin.readline().split()]
def chars(): return list(sys.stdin.readline().strip())
#*************************************************************************
def fvalues(f): return tuple(map(int, f.readline().split()))
def finlst(f): return [int(i) for i in f.readline().split()]
def finp(f): return int(f.readline())
def finpstr(f): return f.readline().strip()
def fwords(f): return [i for i in f.readline().split()]
def fchars(f): return list(f.readline().strip())


######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################

def solve():
     print(fvalues(f))

if __name__ == "__main__":
    global f
    f=open('/home/mohamed/Documents/w.txt','r')
    for i in range(finp(f)):
        solve()
