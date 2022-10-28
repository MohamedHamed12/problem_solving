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
# def valid(i,j):
#         if i<n and i>=0 and j>=0 and j< m :return True #and l[i][j]==1 and visit[i][j]
#         return  False
# def sumn(i,n):
#     return (n-i)*(i+n)/2

######################################################################################
#--------------------------------------vars-----------------------------------------#
######################################################################################
# index=[[1,0],[0,1],[-1,0],[0,-1]]

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


# def solve():
#     global m,n
#     n,m=values()
#     l=[list(input()) for i in range(n)]
#     num=0
    



#     def dffs(i,j):
#         t=0
#         q=[(i,j)]
#         while q:
           
#             rx,ry=q.pop()
#             visit[rx][ry]=False
     
#             for i in index:
#                 k=i[0]+rx;h=i[1]+ry
#                 if valid(k,h)  and visit[k][h] and l[k][h]=='#':
#                     if (k,h) not in q :q.append((k,h))
                    
                        
#     num=0
#     for i in range(n):
#         for j in range(m):
#              if   l[i][j]== '#' :
#                 num+=1
#                 if i==1 and j==m-1 and m>1 and (i+1)*(j+1)==num:return 2

#                 global visit
#                 visit=[[True]*m for i in range(n)]
#                 tmp=[]
#                 for o in index:
#                     k=o[0]+i;h=o[1]+j
#                     if valid(k,h) and l[k][h]=='#':tmp.append((k,h))
#                 if len( tmp)<2:continue
#                 l[i][j]='.'
#                 dfs(tmp[0][0],tmp[0][1])
#                 for k,h in tmp:
#                     if visit[k][h]:return 1
#                 l[i][j]='#'
#     if num<=2:return -1
    
#     else:return 2


# if __name__ == "__main__":
#     # for i in range(inp()):
#         print(solve())
n, m = map(int, input().split())
a = [list(input()) for i in range(n)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
 
def valid(x, y):
    return 0 <= x < n and 0 <= y < m
 
def dfs():
    cnt, p = 0, -1
    for i in range(n):
        for j in range(m):
            if a[i][j] == '#':
                cnt += 1
                p = (i, j)
    if p == -1: 
        return False
        
    vis = [[0]*m for _ in range(n)]
    vis[p[0]][p[1]] = 1
    cnt_vis = 1
    stk = [(p[0], p[1])]
    while stk:
        x, y = stk.pop()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if valid(nx, ny) and not vis[nx][ny] and a[nx][ny] == '#':
                vis[nx][ny] = 1
                cnt_vis += 1
                stk.append((nx, ny))
    return cnt_vis != cnt
 
cnt, flag = 0, 0
f = False
for i in range(n):
    for j in range(m):
        if a[i][j] == '.':
            continue
        cnt += 1
        a[i][j] = '.'
        if dfs(): flag = True
        a[i][j] = '#'
 
if cnt <= 2:
    print(-1)
elif flag:
    print(1)
else:
    print(2)