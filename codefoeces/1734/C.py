import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os
######################################################################################
#--------------------------------------funs here-------------------------------------#
######################################################################################
def values(): return tuple(map(int, sys.stdin.readline().split()))
def inlsts(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(sys.stdin.readline())
def instr(): return sys.stdin.readline().strip()
def words(): return [i for i in sys.stdin.readline().strip().split()]
def chars(): return [i for i in sys.stdin.readline().strip()]
######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################
# def solve():
#     n = inp()
#     s=instr()
#     tmp=set([i+1 for i in range(n)])
#     tot=0
#     for i in range(1,n+1):
#         if s[i-1]=='0':
#             t=min(tmp)
#             while True:
#                 if (i)%t==0:
#                     # tmp.remove(i)
#                     tot+=t
#                     break
#                 t+=1

#         if s[i-1]=='1':
#             for j in range(min(tmp),int(math.sqrt(i)+1)+1):
#                 if (i)%j==0 and j in tmp:tmp.remove(j)
#             if i in tmp:tmp.remove(i)
                
#     print(tot)


# if __name__ == "__main__":
#     for i in range(inp()):
#         solve()
 
for T in range(int(input())):
 
    n = inp()
 
    s = instr()
 
    visited = set()
 
    val = [1000000007]*n
 
    for i in range(n):
        if s[i] == "0":
            # visited.add(i)
            for j in range(i, n, i + 1):
                if s[j] == "0":
                    val[j] = min(val[j], i + 1)
                else:
                    break
 
    final = 0
 
    for i in val:
        if i != 1000000007:
            final += i
 
    print(final)