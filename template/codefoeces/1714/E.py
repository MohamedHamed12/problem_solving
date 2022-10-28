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
def valid(i,j,n,m):
        if i<n and i>=0 and j>=0 and j< m :return True #and l[i][j]==1 and visit[i][j]
        return  False
def sumn(i,n):
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
    l= inlsts()
    f=0
    for i in range(n):
        if l[i]%5 == 0:
            f+=1
            l[i]+=l[i]%10
        else:
            while l[i]%10 != 2: l[i]+=l[i]%10
    if f==n:
            if max(l)==min(l):return "YES"
            else:return "NO"
    elif f>0:return "NO"
    else:
            f=l[0]%20
            for i in range(1,n):
                if l[i]%20!=f:return "NO"
            return "YES"

            




if __name__ == "__main__":
    for i in range(inp()):
        print(solve())
# for _ in range(int(input())):
#     n=int(input())
#     f1=0
#     arr=list(map(int, input().split()))
#     for i in range(n):
#         if arr[i]%5==0:
#             f1+=1
#             arr[i]+=arr[i]%10
#         else:
#             while arr[i]%10!=2:
#                  arr[i]+=arr[i]%10
        
#     if n==f1:
#         if max(arr)==min(arr):
#             print("Yes")
#         else:
#            print("No")
#     elif f1>0 and f1<n:
#             print("No")
#     else:
#         f1=arr[0]%20
#         for i in arr:
#             if i%20!=f1:
#                 print("No")
#                 f1=-1
#                 break
#         if f1!=-1:
#             print("Yes")