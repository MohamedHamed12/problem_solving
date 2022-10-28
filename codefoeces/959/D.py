from cmath import inf
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
lofprimes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449]
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
def record(x):
    t=[]
    for i in lofprimes:
        if x%i==0:
            while  x%i==0: 
                x//=i
            t.append(i)
            if x==1:break
    if x!=1:t.append(x)
    for tmp in t:
      for i in range(tmp,inf,tmp):used[i]=True

def solve():
    global used ,inf
    inf=2000000
    used=[False]*(inf)
    n=input()
    lst=inlsts()
    b=[]
    for i in lst:
        if not used[i]:
            b.append(i)
            record(i)
        else:
            tmp=i+1
            while used[tmp]:tmp+=1
            b.append(tmp)
            record(tmp)
            break
    tmp=2
    while len(b)<len(lst):
        if not used[tmp]:
            b.append(tmp)
            record(tmp)
        tmp+=1
    print(*b)

                





if __name__ == "__main__":
    # for i in range(inp()):
        solve()