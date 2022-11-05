// https://leetcode.com/problems/number-of-provinces

class Solution(object):
    def findCircleNum(self, l):
         n=len(l)
         chlist=[-1]*n
         def find(x):
                while chlist[x]!=-1:
                         if x==chlist[x]:break
                         x=chlist[x]
                return x          
         def union(x,y):
                chlist[x]=y
         def check(x,y):
            m=find(x)
            n=find(y)
            if m!=n:union(x,y)
     
         def check(i,j):
            x=find(i)
            y=find(j)
            if x!=y:union(x,y)

         for i in range(n):
             for j in range(n):
                 if l[i][j]==1 and i!=j:
                        check(i,j)
                        
         return chlist.count(-1)
            