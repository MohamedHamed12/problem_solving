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
    n = inp()
    s=list(instr())
    r1=0
    b1=0
    r2=0
    b2=0
    for i in range(n):
        if i%2==0:
            if s[i]=='b':b2+=1
            if s[i]=='r':r2+=1
        else:
            if s[i]=='b':b1+=1
            if s[i]=='r':r1+=1

    #rbebrb   1r   2=b 
    op1=min(max(r2 ,b1),max(r1,b2))
    print(op1)
    # b=0;r=0
    # s=ss
    # for i in range(n-1,0,-1):
    #     if s[i-1]==s[i]:
    #           if s[i-1]=='r':s[i-1]='b';b+=1
    #           else:s[i-1]='r';r+=1
    # ans=min(min(r, b),ans)
    # print(ans)






if __name__ == "__main__":
    # for i in range(inp()):
        solve()