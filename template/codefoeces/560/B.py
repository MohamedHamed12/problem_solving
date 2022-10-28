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
    a1,b1=sorted(values())
    a2,b2=sorted(values())
    a3,b3=sorted(values())
    if a1>=a2+a3 and b1>=max(b2,b3):print("YES");return
    if b1>=a2+a3 and a1>=max(b2,b3):print("YES");return


    if b1>=b2+b3 and a1>=max(a2,a3):print("YES");return
    if a1>=b2+b3 and b1>=max(a2,a3):print("YES");return

    if b1>=b2+a3 and a1>=max(a2,b3):print("YES");return
    if a1>=b2+a3 and b1>=max(a2,b3):print("YES");return

    if b1>=a2+b3 and a1>=max(b2,a3):print("YES");return
    if a1>=a2+b3 and b1>=max(b2,a3):print("YES");return

    print("NO")


if __name__ == "__main__":
    # sys.stdin = open('/home/mohamed/Documents/w.txt','r')
    # for i in range(inp()):
        solve()
'''
84 99
82 54
73 45
'''