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
def inlsts(): return [int(i) for i in  sys.stdin.readline().split()]
def inp(): return int(input())
def inps(): return int(sys.stdin.readline())
def instr(): return input()
def stlst(): return [i for i in input().split()]
    
 
# ######################################################################################
# #--------------------------------------code here-------------------------------------#
# ######################################################################################
# def cnt(l,x,i):
#     tot=0
#     while i<len(l)-1:
#         if l[i]==x:tot+=1
#         else:return tot
#         i+=1
# def finish(l,i):

# def get(l,x,i):
#      tem=l.cnt(l,x,i)
#      if tem+1>2:
#             l=l[:i]+l[tem+i:]
#             finih(l,i)

    
def solve():
      n,k,x=values()
      l=inlsts()
      mx=0
      ele=[]
      elecount=[]
      c=itertools.groupby(l)
      for i ,j in c:
            ele.append(i)
            elecount.append(len(list(j)))
      for i in range(len(ele)):
            if ele[i]==x and elecount[i]==2:
                l,r=i-1,i+1
                temp=2
                while l>=0 and r<=len(ele)-1:
                    if ele[l]==ele[r]:
                        s=elecount[r]+elecount[l]
                        if s>2:
                            temp+=s
                            l-=1;r+=1
                        else:break
                    else:break
                mx=max(mx,temp)
            

      print (mx)

 
solve()
# n,k,x=values()
# c=inlst()
# ele=[]
# elecounters=[]
# gg=itertools.groupby(c)
# for key, count in gg:
#     ele.append(key)
#     elecounters.append(len(list(count)))
# ans=0
# for i in range(len(ele)):
#     if ele[i]==x and elecounters[i]==2:
#         backward=i-1
#         forward=i+1 
#         temp= 2
#         while backward>=0 and forward <= len(ele)-1:
#             bla=elecounters[backward]+elecounters[forward]
#             if ele[backward]==ele[forward] and bla >=3:
#                 temp+=bla
#                 backward-=1
#                 forward+=1
#             else:
#                 break
#         ans=max(ans, temp)
#         #print(temp, i)
 
# print(ans) #final answer