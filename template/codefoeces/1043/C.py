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
    s=instr()
    n=len(s)
    l=[]
    for i in range(1,n):
        if s[i]!=s[i-1]:l.append(1)
        else:l.append(0)
    if s[-1]=='a':l.append(1)
    else:l.append(0)
    print(*l)


if __name__ == "__main__":
        solve()
# s = input()
# n = len(s)
# res = []
# for i in range(1,n):
#     if s[i]!=s[i-1]:
#         res.append(1)
#     else:
#         res.append(0)
# if s[n-1]=='a':
#     res.append(1)
# else:
#     res.append(0)
# #print(s)
# for i in res:
#     print(i,end=' ')