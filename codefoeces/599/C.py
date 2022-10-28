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
    l = inlst()

    tot = 0
    sl = sorted(l)

    ###############################
    tem = 0
    for i in range( n):
        
        tem += sl[i]-l[i]
        if tem == 0:
            tot += 1
#    i=0
#    while i<n:
#         if l[i]==sl[i]:
#             tot+=1
#             i+=1
#         else:
#             i=bisect.bisect_left(sl,l[i])+1
#             tot+=1

    print(tot)


solve()


# n, s, v = int(input()), 0, 0

# a = list(map(int, input().split()))
# m=zip(a, sorted(a))
# for ai, bi in m:

#     s += bi - ai

#     v += not s

# print(v)
# a=inlst()
# m=(zip(a, sorted(a)))
# for i in m:print(i)