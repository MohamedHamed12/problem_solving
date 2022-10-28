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
  
# def solve():
#    nn=n=inp()
#    tot=[]
#    tem=1
#    if n<4:
#         t=[1]*(n-1)
#         t.append(n)
#         print(*t)
#         return
#    while n!=0:
#         m=math.ceil(n/2)
#         tot+=[tem]*m
#         n=n//2
#         tem*=2
# #    if nn%2!=0:nn-=1
# #    tot.append(nn)
# #    print(*tot)

 
# solve()
# def main(n):
#     # n = int(input())
 
#     k = 1
#     ans = []
#     while True:
#         if n == 3:
#             ans += [k, k, 3 * k]
#             break
#         elif n == 2:
#             ans += [k, 2 * k]
#             break
#         elif n == 1:
#             ans += [k]
#             break
#         elif n == 0:
#             break
#         else:
#             m = (n + 1) // 2
#             ans += [k] * m
#             k *= 2
#             n //= 2
 
#     print(*ans)
 
 
# if __name__ == "__main__":
#   for i in range(2,20):
#       main(i)
def main():
    n = int(input())
 
    k = 1
    ans = []
    while n >= 4:
        m = (n + 1) // 2
        ans += [k] * m
        k *= 2
        n //= 2
 
    if n == 3:
        ans += [k, k, 3 * k]
    elif n == 2:
        ans += [k, 2 * k]
    elif n == 1:
        ans += [k]
 
    print(*ans)
 
 
if __name__ == "__main__":
    main()