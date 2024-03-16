import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os
######################################################################################
#--------------------------------------func-----------------------------------------#
######################################################################################
def valid(i,j,n,m):
        if i<n and i>=0 and j>=0 and j< m :return True #and l[i][j]==1 and visit[i][j]
        return  False
def sumn(i,n):
    return (n-i)*(i+n)/2
def sqfun(a,b,c):
    return (-b+math.sqrt(b*b-4*a*c))/2*a
def getprime(num):     
        if  all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):return  True
           
######################################################################################
#--------------------------------------vars-----------------------------------------#
######################################################################################
# index=[[1,0],[0,1],[-1,0],[0,-1]]
# primes=[2,3,5,7,11,13,17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
#  109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
#   241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383,
#    389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
#     547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683,
#      691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857,
#       859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
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

def solve(): 
    n,m=values()
    d=collections.defaultdict(list)
    for i in range(m):
        u,v,w=values()
        d[w].append((u,v))
    dp=[0]*(n+1)
    
    for w in sorted(d.keys()):
        l=[]
        for u,v in d[w]:
            l.append((dp[u],v))
        for dpu,v in l:
            dp[v]=max(dpu+1,dp[v])
     
    print(max(dp))
solve()
# def prob():
#     n,m = [int(x) for x in input().split()]
#     gr = [[] for i in range(10**5 + 1)]
 
#     for i in range(m):
#         u,v,w = [int(x) for x in input().split()]
#         gr[w].append((u,v))
 
#     dp = [0] * (n+1)
 
#     for i in gr:
 
#         l = []
 
#         for x,y in i:
#             l.append((dp[x],y))
 
#         for x,y in l:
#             dp[y] = max(dp[y] , x+1)
 
#     print(max(dp))
 
# prob()