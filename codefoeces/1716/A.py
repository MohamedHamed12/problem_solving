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

def solve(n):
   
    if n %3==0:
        print(n//3)
        return
 
    if n==1:
        print(2);return 

    tem=2
    while (n-tem)%3!=0:
        tem+=2
    j=tem//2+(n-tem)//3
    print(str(j))
   



n=int(input())
for i in range(n):
        k = inp()
        solve(k)