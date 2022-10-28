import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os


# sys.setrecursionlimit(10000)
def values(): return tuple(map(int, sys.stdin.readline().split()))


def inlst(): return [int(i) for i in sys.stdin.readline().split()]


def inp(): return int(sys.stdin.readline())


def inpstr(): return sys.stdin.readline().strip()


def words(): return [i for i in sys.stdin.readline().split()]


def chars(): return list(sys.stdin.readline().strip())


def solve():
    n,q=values()
    d= collections.defaultdict(list)
    arr=[2**30-1]*n
    l=[0]*n
    for i in range(q):
        a,b,x=values()
        a-=1;b-=1
        arr[a]&=x  ; arr[b]&=x
        d[a].append((b,x))
        d[b].append((a,x))
    for i in range(n):

        for j ,x in d[i]:
            if i != j:
              l[i]|=x^arr[j]
            else:
              l[i] =x
        arr[i]=l[i]
    print(*l)



if __name__ == "__main__":
    # sys.stdin = open('/home/mohamed/Documents/w.txt', 'r')
    # for i in range(inp()):
        solve()

# import sys
#
# n, Q = list(map(int, sys.stdin.readline().strip().split()))
# m = [0] * n
#
# M = [2 ** 30 - 1] * n
# L = [[] for i in range(0, n)]
# for q in range(0, Q):
#     i, j, x = list(map(int, sys.stdin.readline().strip().split()))
#     i -= 1; j -= 1
#
#     M[i] &= x
#     M[j] &= x
#     L[i].append((j, x))
#     L[j].append((i, x))
# for i in range(0, n):
#     for (j, x) in L[i]:
#         if j != i:
#             m[i] |= x ^ M[j]
#         else:
#             m[i] = x
#     M[i] = m[i]
# print(*m)