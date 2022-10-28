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


def solve():
    v = inp()
    l = values()
    amount = min(l)
    for i in range(8,-1,-1):
        if l[i]==amount:unit=i;break
    if v < amount:
        print(-1) ;return  
    rem = v-(v//amount)*amount
    s=[0]*9
    s[unit]+=(v//amount)
    for i in range(8,unit,-1):
        while l[i]-amount<=rem:
            s[i]+=1;s[unit]-=1
            rem-=l[i]-amount
    ss=''
    for i in range(8,-1,-1):
        ss+=s[i] *str(i+1)
    print(ss)


if __name__ == "__main__":
    # for i in range(inp()):
    (solve())