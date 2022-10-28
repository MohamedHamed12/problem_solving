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
def sol(eq1,eq2):
    x1, y1 ,z1=eq1
    x2, y2,z2=eq2
    det=x1*y2-x2*y1
    if det==0:return 'imp'
    x=(z1*y2-z2*y1)//det
    y=(x1*z2-x2*z1)//det
    return (x,y)
def solve():
    n,k,d1,d2 =values()
    if n%3!=0:return "no"

    nn=n//3
    for i,j in [(1,1),(1,-1),(-1,1),(-1,-1)]:
           tmp=sol((1,-1,d1*i),(1,2,k+d2*j))
           if tmp=="imp":continue
           x,y=tmp
           z=k-x-y
           if x<=nn and x>-1 and y<=nn and y>-1 and z<=nn and z>-1 and x+y+z==k and abs(x-y)==d1 and abs(y-z)==d2:return "yes"
    return "no"
for i in range(inp()):
    print(solve())