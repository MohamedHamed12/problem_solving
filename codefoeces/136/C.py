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
def inlsts(): return [int(i) for i in  sys.stdin.readline().split()]
def inp(): return int(input())
def inps(): return int(sys.stdin.readline())
def instr(): return input()
def stlst(): return [i for i in input().split()]
    
 
######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################
  
def solve():
 inp()
 l=inlst()
 if max(l)==1:
        l.pop()
        l.append(2)
        print(*l)
        return
 l[l.index(max(l))]=1
 print(*sorted(l))

 
solve()
# n=int(input())
# l=[int(_) for _ in input().split()]
# if n!=1:
#     l.sort()
#     if l[n-1]!=1:
#         print(1,*l[:n-1])
#     else:
#         print(*l[:n-1],2)
# else:
#     if l[0]==1:
#         print(2)
#     else:
#         print(1)
# def main():
#     n=int(input())
#     L=list(map(int,input().split()))
#     if max(L)==1:
#         L[L.index(max(L))]=2
#     else:
#         L[L.index(max(L))]=1
#     L.sort()    
#     print(' '.join(map(str, L)))   
# main()