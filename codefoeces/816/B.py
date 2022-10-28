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
    n, k, q = values()
    l = [0]*(200003)
    mn, mx = 200003, 0
    for i in range(n):
        a, b = values()
        mn = min(mn, a)
        mx = max(mx, b)
        l[a] += 1
        l[b+1] -= 1
    arr = [0]*(200003)
    for i in range(200001):
        l[i+1] += l[i]
        if l[i] >= k:
            arr[i] = 1

    for i in range(1,200001):
        arr[i] += arr[i-1]
    for _ in range(q):
        a, b = values()
        tot = arr[b]-arr[a-1]
        # for j in range(a,b+1):
        # if l[j]>=k:tot+=1
        sys.stdout.write(str(tot)+"\n")


solve()