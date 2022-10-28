import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os
######################################################################################
#--------------------------------------funs here-------------------------------------#
######################################################################################
def values(): return tuple(map(int, sys.stdin.readline().split()))
def inlsts(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(sys.stdin.readline())
def instr(): return sys.stdin.readline().strip()
def words(): return [i for i in sys.stdin.readline().strip().split()]
def chars(): return [i for i in sys.stdin.readline().strip()]
######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################


ccc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def solve():
    n, k = values()
    kk = k
    s = instr()
    c = collections.Counter(s)

    tot = ""
    m = 0
    for i in ccc:
        if m == n//kk:
            tot += i*(kk- len(tot))
            k = 0
            break

        if c[i] < k:
            tot +=i* (k-c[i])
            k = c[i]
        if k <= 0:
            break

        m += 1
    print("".join(sorted(list(tot),reverse=True)))


if __name__ == "__main__":
    for i in range(inp()):
        solve()