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
    option=[0]*123+[1]*(9754)
    for i in range(123,len(option)):
        tmp=f'{i:04d}'
        if len(set(tmp))!=4:option[i]=0
    for _ in range(inp()):
        num,b,c=input().split()
        b=int(b);c=int(c)
        for i in range(123,len(option)):
            if option[i]==1:
                tmp=f'{i:04d}'
                m= len(set(tmp)& set(num))
                o=sum([h==k for h,k in zip(num,tmp) ])
                if m-o!=c or o!=b:option[i]=0
               
    if sum((option))==0:return 'Incorrect data'
    elif sum((option))>1: return 'Need more data'
    else:return f'{option.index(1):04d}'



if __name__ == "__main__":
    # for i in range(inp()):
        print(solve())