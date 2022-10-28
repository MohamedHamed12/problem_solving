import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os
######################################################################################
#--------------------------------------func-----------------------------------------#
######################################################################################


def valid(i, j, n, m):
    if i < n and i >= 0 and j >= 0 and j < m:
        return True  # and l[i][j]==1 and visit[i][j]
    return False


def sumn(i, n):
    return (n-i)*(i+n)/2

######################################################################################
#--------------------------------------vars-----------------------------------------#
######################################################################################
# index=[[1,0],[0,1],[-1,0],[0,-1]]

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
    tot = 0
    arr = inlsts()
    tmp = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] <= tmp:
            tmp = arr[i]
        else:
            s=set(arr[:i+1])
            for i in range(n-1, -1, -1):
                if arr[i] in s:return len(set(arr[:i+1]))
    return 0


if __name__ == "__main__":
    for i in range(inp()):
        print(solve())
# lis = [1]*n

#     # Compute optimized LIS values in bottom up manner
#         for i in range(1, n):
#             for j in range(0, i):
#                 if arr[i] > arr[j] and lis[i] < lis[j] + 1:
#                     lis[i] = lis[j]+1

#         # Initialize maximum to 0 to get
#         # the maximum of all LIS
#         maximum = 0

#         # Pick maximum of all LIS values
#         for i in range(n):
#             maximum = max(maximum, lis[i])

#         return maximum
#         # tot=[nums[0]]
#         # nums.pop(0)
#         # for  i in range(n-1):
#         #     if nums[i]>=tot[-1]:tot.append(nums[i])
#         #     else:tot[bisect.bisect_left(tot,nums[i])]=nums[i]
#         # return n-len(tot)