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
def lcm(a,b):
    return a*b//math.gcd(a,b)
def solve():
    l,a,b=values()
    mn=min(a,b)-1
    k=l//lcm(a,b)
    tot=(k-1)*(1+mn)+mn
    tot+=min(l,k*(lcm(a,b))+mn)-k*lcm(a,b)+1
    t1=tot//math.gcd(tot,l)
    t2=l//math.gcd(tot,l)
    # print(f'{tot}/{l}')   
    print(f'{t1}/{t2}')    

if __name__ == "__main__":
        solve()