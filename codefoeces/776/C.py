import collections
from email.policy import default
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
    n ,k=values()
    l=inlsts()
    if abs(k)>1:
            valid = [k ** i for i in range(0, math.ceil(math.log(n * 1e9) / math.log(abs(k))) + 1)]

        # valid=[k**i for i in range(50)]
    elif k==-1 :
          valid=[1,-1]
    else:
        valid=[1]
    s=0
    ans=0
    d=collections.defaultdict(int)
    d[0]=1

    for i in l:
        s+=i
        for j in valid:
             ans+=d[s-j]
        d[s]+=1
    print(str(ans))





solve()


# import math
# n, k = [int(i) for i in input().split()]
# a = [int(i) for i in input().split()]


# if abs(k) > 1:
#     valid = [k ** i for i in range(0, math.ceil(math.log(n * 1e9) / math.log(abs(k))) + 1)]
# elif k == -1:
#     valid = [1, -1]
# else:
#     valid = [k]
 
# s = 0
# ans = 0
# count = {s : 1}
# for i in a:
#     s += i
#     # for j in valid:
#         if count.get(s - j):
#             ans += count[s - j]
#     if count.get(s):
#         count[s] += 1
#     else:
#         count[s] = 1
# print(ans)