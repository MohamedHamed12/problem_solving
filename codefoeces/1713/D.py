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
    l=[i for i in range(1,2**n+1)]
    while n>1:
            tem=[]
            for i in range(0,2**n,4):
                print('?',l[i],l[i+2])
            for i in range(0,2**n,4):
                ans= inp()
                if ans==0:
                    tem.append(l[i+1]);tem.append(l[i+3])
                elif ans==1:
                    tem.append(l[i]);tem.append(l[i+3])
                elif ans ==2:

                    tem.append(l[i+2]);tem.append(l[i+1])
            l=tem
        
            n-=1
    print('?',l[0],l[1])
    ans=inp()
    if ans ==1:print('!',l[0])
    else:print('!',l[1])
    




if __name__ == "__main__":
    for i in range(inp()):
        solve()
# import sys
# def solve():
#     n = int(input())
#     ls = [i for i in range(1, 2 ** n + 1)]
   
#     while n > 1:
#         curr = []
#         for i in range(0, 2 ** n, 4):
#             print('?', ls[i], ls[i+2])
 
#         for i in range(0, 2 ** n, 4):
#             r = int(input())
#             if r == 1:
#                 curr.append(ls[i])
#                 curr.append(ls[i+3])
#             elif r == 2:
#                 curr.append(ls[i+2])
#                 curr.append(ls[i+1])
#             else:
#                 curr.append(ls[i+1])
#                 curr.append(ls[i+3])
#         n -= 1
#         ls = curr


#     print('?', ls[0], ls[1])
#     r = int(input())
#     if r == 1:
#         print('!', ls[0])
#     else:
#         print('!', ls[1])
    
# t = int(input())
# for _ in range(t):
#     solve()