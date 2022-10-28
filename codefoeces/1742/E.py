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


def solve():
    n, q = values()
    l = values()
    qq = values()
    m = [0]*(n+1)
    dp = [0]*(n+1)
    for i in range(n):
        dp[i+1] = dp[i]+l[i]
        m[i+1] = max(m[i], l[i])
    tot = [0]*q
    for i in range(q):
        ind = bisect.bisect_right(m, qq[i])
        tot[i] = dp[ind-1]
    print(*tot)


if __name__ == "__main__":
    for i in range(inp()):
        solve()