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
    
    n = inp()
    l=inlst()
    if len(set(l))>n-2:print ("NO");return
    print("YES")
    e=sorted(enumerate(l,start=1),key=lambda x:x[1])
    print (*[i for i,j in e])
    tem=1
    for i in range(1,n):
        if tem==3:break
        if e[i][1]==e[i-1][1]:
            e[i],e[i-1]=e[i-1],e[i]
            tem+=1
            print (*[i for i,j in e])


        


if __name__ == "__main__":
        solve()