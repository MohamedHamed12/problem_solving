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
def values(): return list(map(int, sys.stdin.readline().split()))
def inlsts(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(sys.stdin.readline())
def instr(): return sys.stdin.readline().strip()
def words(): return [i for i in sys.stdin.readline().strip().split()]
def chars(): return [i for i in sys.stdin.readline().strip()]
######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################

def sevee(n):

    tmp=0
    for i in range(2,n): 
        if ss[i]==0:
            tmp=0
            if i==2:tmp=1
            j=i
            while j<n:
                ss[j]=tmp
                tmp+=1
                j*=2
        



def solve():
    global ss
    n = inp()
    ss=[0]*(n+1)
    sevee(n+1)

    l=values()
    tmp=0
    for  i in range(n):
        while l[i]%2==0:l[i]//=2;tmp+=1
    if tmp>=n:return 0
    tmp=n-tmp
    tot=0
    for i in sorted(ss,reverse=True):
        tmp-=i
        tot+=1
        if tmp<=0:return tot
        if i==0:return -1



if __name__ == "__main__":
   
    # print(ss[:20])
    for i in range(inp()):
        print(solve())