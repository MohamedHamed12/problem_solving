// https://leetcode.com/problems/rotting-oranges

from sys import maxsize

class Solution:
    def orangesRotting(self, grid) :
        n=len(grid);m=len(grid[0])
        cost=[[-1]*m for i in range(n)]
        visit=[[True]*m for i in range(n)]
        def vald(i,j):
            if i<n and i>=0 and  j<m and j>=0 and visit[i][j] :  return True  
            return False
        def dfs(q):
            nonlocal cost
            tot=1
            q2=[]
            while q:
                h,k=q.pop()
                l=[[h+1,k],[h,k+1],[h-1,k],[h,k-1]]
                for r in l:
                     if vald(r[0],r[1]) and ((r not in q) and (r not in q2))   :
                         if grid[r[0]][r[1]]==1:
                            q2.append(r)
                            cost[r[0]][r[1]]=tot
                            grid[r[0]][r[1]]=2 
                
                visit[h][k]=False 
                

                
                if not  q:
                    q=q2.copy()
                    q2.clear()
                    tot+=1
                
        q=[]
        for i in range(n):
            for j in range(m) :
                     if grid[i][j]==2:q.append([i,j])
                        
        dfs(q)
        tem=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:return -1
                tem=max(tem,cost[i][j])
                
        return tem
                
