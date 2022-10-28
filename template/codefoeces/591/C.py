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

def change(f,r):
    
        if f==r:return 0
        if l[f]==l[r]:
            for i in range(f+1,r):
                l[i]=l[f]
            return (r-f)//2

        else:
            m=(f+r+1)//2
            for i in range(f+1,m):
                l[i]=l[f]
            for i in range(m,r):
                    l[i]=l[r]
            return (r-f-1)//2

        

def solve():
   
    n = inp()
    global  l

    l=inlsts()
    ans=0
    cur=0
    for i in range(n):
        if  i==n-1 or l[i]==l[i+1] :
            ans=max(ans,change(cur,i))
            cur=i+1
    
    print(ans) 
    print (*l)

if __name__ == "__main__":
    # for i in range(inp()):
        solve()
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright  2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.



# n = int(input())

# a = [i for i in input().split()]

# def change(l, r):
#     global a

#     if l == r:
#         return 0

#     if a[l] == a[r]:
#         for i in range(l+1, r):
#             a[i] = a[l]
#         return (r-l)//2
#     else:
#         m = (l+r+1)//2

#         for i in range(l+1, m):
#             a[i] = a[l]

#         for i in range(m, r):
#             a[i] = a[r]

#         return (r-l-1)//2


# answ = 0
# current = 0

# for i in range(n):
#     if i == n-1 or a[i] == a[i+1]:
#         answ = max(answ, change(current, i))
#         current = i+1

# print(answ)
# print(" ".join(a))