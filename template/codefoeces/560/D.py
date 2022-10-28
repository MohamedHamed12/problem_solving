import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os

# sys.setrecursionlimit(10000)

def values(): return tuple(int(i) for i in sys.stdin.readline().split())
def inlst(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(sys.stdin.readline())
def inpstr(): return sys.stdin.readline().strip()
def words(): return [i for i in sys.stdin.readline().split()]
def chars(): return list(sys.stdin.readline().strip())

def equal(a):
    if len(a)%2==1:return a
    k=equal(a[:len(a)//2])
    h=equal(a[len(a)//2:])
    if k>h:
        return h+k
    return k+h
    # if len(a)%2==1:
    #     if a == b: return True
    #     return False
    # if a==b:return True
    # a1=a[:(len(a)//2)]
    # a2=a[(len(a)//2):]
    # b1=b[:len(a)//2];b2=b[len(a)//2:]
    # if a1==b1:return equal(a2,b2)
    #
    # elif a1==b2:return equal(a2,b1)
    # return False
def solve():
    a=inpstr()
    b=inpstr()
    if len(a)!=len(b):return "NO"
    return "YES" if   equal(a)==equal(b) else "NO"





if __name__ == "__main__":
#     # sys.stdin = open('/home/mohamed/Documents/w.txt','r')
#     for i in range(inp()):
       print( solve())