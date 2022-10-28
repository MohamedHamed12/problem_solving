import collections
from email.policy import default
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


# ######################################################################################
# #--------------------------------------code here-------------------------------------#
# ######################################################################################
def get(st,n):
    l[st].append(0)
    l[st+1].append(st)
    l[st+2].append(st+1)
    l[st+3].append(st+2)
    l[st+3].append(st)
    l[st+4].append(st+1)
    l[st+4].append(st+2)
    l[st+4].append(st+3)
    for i in range(st+5,st+5+n-3,2):
        tmp=list(l.keys())
        for j in tmp:
            l[i].append(j)
        for j in tmp:
            l[i+1].append(j)



        
    

    

def solve():
    global l
    n = inp()
    l=collections.defaultdict(list)
    st=1
    if n%2==0: print ("NO");return 
    else:
       
        print("YES")
        if n==1:
            print(2 ,1);print(1, 2)
            return 
        print((n+2)*2,n*n+2*n)
        get(st,n)
        l[1].remove(0)
        mx=max(list(l.keys()))
        l[1].append(mx+1)
        for i in l:
            for j in l[i]:
              print(i,j)

        l=collections.defaultdict(list)
        
        get(mx+1,n)
        l[mx+1].remove(0)
        for i in l:
            for j in l[i]:
              print(i,j)
        

        
    

if __name__ == "__main__":
    # for i in range(inp()):
        solve()
# k = int(input())
# if k == 1:
#   print('YES')
#   print(2, 1)
#   print(1, 2)
# elif k%2:
#   print('YES')
#   print(2*k + 4, k*k + 2*k)
#   matrix = [[False]*(2*k + 4) for _ in range(2*k + 4)]
#   for i in range(k+1):  
#     for j in range(i+1, k+1):
#       matrix[i][j] = True
#   for i in range(k+2, 2*k + 3):
#     for j in range(i+1, 2*k + 3):
#       matrix[i][j] = True
#   need = 0
#   i = 0
#   matrix[k+1][-1] = True
#   while need != k - 1:
#     matrix[k+1][2*i] = True
#     matrix[k+1][2*i + 1] = True
#     matrix[-1][2*i + k + 2] = True
#     matrix[-1][2*i + k + 3] = True
#     matrix[2*i][2*i + 1] = False
#     matrix[2*i + k + 2][2*i + k + 3] = False
#     need += 2
#     i += 1
#   for i in range(2*k + 4):
#     for j in range(2*k + 4):
#       if matrix[i][j]: print(i+1, j+1)
# else:
#   print('NO')