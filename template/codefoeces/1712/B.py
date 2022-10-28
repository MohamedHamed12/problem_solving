import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os


def solve():
        nnn = int(input())
    # if n==1:return[1]
    # elif n==2:return[2,1]
    # else:
        l=[]
        m=nnn
        k=nnn-1
        for i in range(nnn//2):
            l.append(k-2*i)
            l.append(m-2*i)
            # k,m=m,k

        if nnn%2==0:print(*l[::-1]) 
        else:print(*(l+[1])[::-1]) 



if __name__ == "__main__":
    for i in range(int(input())):
       (solve()) 
# from math import gcd


# print(gcd(5,4))