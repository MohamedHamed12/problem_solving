// https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution:
    def pacificAtlantic( self,heights):    
        n=len(heights);m=len(heights[0])
        visit=[[True]*m for i in range(n)]
        def vald(i,j):
            if i<n and i>=0 and  j<m and j>=0 and visit[i][j] :  return True  
            return False
        temi=0;temj=0
        def give(i,j,i2,j2):
             if i2==temi or j2==temj :return True
             if heights[i2][j2]>=heights[i][j]:return True
             return False
        def dfs(i,j):
            q=[[i,j]]
            while q:
                h,k=q.pop()
                l=[[h+1,k],[h,k+1],[h-1,k],[h,k-1]]
                for r in l:
                     if vald(r[0],r[1]) and r not in q  :
                         if give(h,k,r[0],r[1]): q.append(r)
                       
                visit[h][k]=False                              
        for j in range(m):
            dfs(0,j)
        for i in range(n) :
            dfs(i,0)
        v=visit.copy()
        visit=[[True]*n for i in range(n)]
        temi=n-1;temj=m-1
        for j in range(m):
            dfs(n-1,j)
        for i in range(n) :
            dfs(i,m-1)
        ret=[]
        for i in range(n):
            for j in range(m):
                if (not v[i][j] )and (not visit[i][j]):ret.append([i,j])
        return ret

