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
def get(l1,l2): 
            tot=0
            if l1[-1]<l2[-1]:
                tot+= l1.pop()
                while l2 :
                    tot += l2.pop(0)*2
                    if l1:   tot += l1.pop(0)*2
            else:
                tot+= l2.pop()
                while l1 :
                    tot += l1.pop(0)*2
                    if l2:   tot += l2.pop(0)*2
            
            return tot
                
 


def solve():
    n = inp()
    l = values()
    val = values()
    val0 = []
    val1 = []
    for i in range(n):
        if l[i] == 0:
            val0.append(val[i])
        else:
            val1.append(val[i])
    val0 = sorted(val0, reverse=True)
    val1 = sorted(val1, reverse=True)

    def s(l1, l2):
        tot = l1.pop()
      
        while l2:
            tot += l2.pop(0)*2
            tot += l1.pop(0)*2
             
        while l1:
                tot += l1.pop(0)
        return tot


    if len(val0)==len(val1):return get(val0,val1)
    if len(val0) >len(val1):  return s(val0, val1)
      
    else: return s(val1, val0)
       
   


if __name__ == "__main__":
    for i in range(inp()):
        print(solve())