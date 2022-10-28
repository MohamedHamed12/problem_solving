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
    mod = (7+10**9)
    n, k = values()
    l = []
    mx = 0
    dp = []
    s = []
    tem=0
    for i in range(n):
        a, b = values()
        mx = max(mx, b)
        l.append((a, b))
    for i in range( mx+2):
        if i < k:
            dp.append(1)
        else:
            dp.append((dp[-1]+dp[-k]%mod) )
        tem+=(dp[-1]%mod)
        s.append(tem )

    for a, b in l:
        print((s[b]-s[a-1])%mod)


if __name__ == "__main__":
    solve()