import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os

# sys.setrecursionlimit(10000)

def values(): return tuple(map(int, sys.stdin.readline().split()))
def inlst(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(sys.stdin.readline())
def inpstr(): return sys.stdin.readline().strip()
def words(): return [i for i in sys.stdin.readline().split()]
def chars(): return list(sys.stdin.readline().strip())


def solve():
     c=inpstr()
     n=len(c)
     y=1
     if c[0] == '-':
         y =(float(c[1:]) * -1)
         c=c[1:]
     c = list(c)
     ind=len(c)
     if '.' in c :
         c.append('0')
         c.append('0')
         c = list(c)
         ind=c.index('.')
         c=c[:ind+3]
         c="".join(c)
     else:
      c.append('.')
      c.append('0')
      c.append('0')

     i=ind-3
     c=list(c)
     while i>0:
         c.insert(i,',')
         i-=3


     c="".join(c)
     if y<0:
          m='('+'$'+c+')'
     else:
        m='$'+c
     print(m)

'''
-12357444245.326585
'''



if __name__ == "__main__":
    # sys.stdin = open('/home/mohamed/Documents/w.txt','r')
    # for i in range(inp()):
        solve()
# l=[1,2,3,4]
# l2=[3,5,8]
# print(set(l)&set(l2))
# print(inter)