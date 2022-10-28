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
def inlsts(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(input())
def inps(): return int(sys.stdin.readline())
def instr(): return input()
def stlst(): return [i for i in input().split()]


######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################

def solve():
      n,t=values()
      color={i+1:-1 for i in range(n) }
      d=collections.defaultdict(list)
      for i in range(t):
            u,v=value()
            d[u].append(v)
            d[v].append(u)
      def dfs(root,col):
            color[root]=col
            for i in d[root]:
                if color[i]==-1:
                    dfs(i,1-col)
      for i in range(1,n+1):
            if color[i]==-1:
                dfs(i,1)
      tot=0
      for i in range(1, n+1):
            for j in d[i]:
                if color[i]==color[j]:tot+=1
      tot=tot//2
      if (n-tot)%2==0:
             print(tot)
      else:print((tot)+1)
            
            
    



if __name__ == "__main__":
        solve()




 
# n, m = map(int, input().split())
 
# graph = collections.defaultdict(list)
# colors = {i:-1 for i in range(1,n+1)}
# visited = set()
 
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
 
# def dfs(node, color):
#     colors[node] = color
#     for v in graph[node]:
#         if colors[v] == -1:
#             dfs(v, 1-color) 
 
# for v in range(1, n+1):
#     if colors[v] == -1:
#         dfs(v, 1)
 
# count = 0
# for v in range(1, n+1):
#     for node in graph[v]:
#         if colors[node] == colors[v]:
#             # print(999, node, v)
#             count +=1
 
# count = count//2
# print(count if (n-count)%2==0 else count+1)
# # print(math.ceil(count/2 ))