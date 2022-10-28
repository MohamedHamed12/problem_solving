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
def check(x1,y1,r1,x2,y2,r2,R2):
    d=((x1-x2)**2+(y1-y2)**2)**(0.5)
    if r1+R2  <=d:return True
    if d+r1<=r2 or  d+R2<=r1  :return True
    
def solve():
    x1,y1,r1,R1=values()
    x2,y2,r2,R2=values()
    ans=0
    if check( x1,y1,r1,x2,y2,r2,R2):ans+=1
    if check( x1,y1,R1,x2,y2,r2,R2):ans+=1
    # if check( x1,y1,R1,x2,y2,r2):ans+=1
    # if check( x1,y1,R1,x2,y2,R2):ans+=1

    # if check( x2,y2,r2,x1,y1,r1):ans+=1   #1
    # if check( x2,y2,R2,x1,y1,r1):ans+=1
    if check( x2,y2,r2,x1,y1,r1,R1):ans+=1   #2
    if check( x2,y2,R2,x1,y1,r1,R1):ans+=1
  

 

    print(ans)


if __name__ == "__main__":
    # for i in range(inp()):
        solve()