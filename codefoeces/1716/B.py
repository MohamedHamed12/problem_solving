import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os


def solve(n):
   
    l=[i for i in range(1,n+1)]
    print(n)
    for i in range(n-1,-1,-1):
        t=l.copy()
        m=t.pop(i)
        t.append(m)
        print(*t)


nn=int(input())

for i in range(nn):
        n = int(input())
        solve(n)