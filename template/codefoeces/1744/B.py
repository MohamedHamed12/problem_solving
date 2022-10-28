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
    n ,q=values()
    l=values()
    odd=0;even=0
    nev=0;nod=0
    for i in range(n):
        if l[i]%2==0:even+=l[i];nev+=1
        else:odd+=l[i];nod+=1
      
    for i in range(q):
        a,b=values()
        if a==0:
            even+=b*nev
            print (even+odd)
        else:
            odd+=b*nod
            print(odd+even)
        if b%2!=0:
            if a==0:
                 odd+=even;even=0
                 nev=0;nod=n
            else:
                 even+=odd;odd=0
                 nod=0;nev=n
               


if __name__ == "__main__":
    for i in range(inp()):
        solve()