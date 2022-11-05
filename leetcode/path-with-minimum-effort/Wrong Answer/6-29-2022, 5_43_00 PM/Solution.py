// https://leetcode.com/problems/path-with-minimum-effort

from sys import maxsize


class Solution:
    def minimumEffortPath(self, grid) :





        n=len(grid)
        cost=[[maxsize]*n for i in range(n)]
        visit=[[True]*n for i in range(n)]

        def vald(i,j):
            if i<n and i>=0 and  j<n and j>=0 and visit[i][j]:
                return True
            else:
                return False

       
        q=[[0,0]]
        cost[0][0]=grid[0][0]
        while q:
            h,k=q.pop()
            if vald(h+1,k)  :
                    q.append([h+1,k]) 
                    cost[h+1][k]=min(cost[h+1][k],abs(grid[h+1][k]-grid[h][k]))
            if  vald(h,k+1)  :
                    q.append([h,k+1])  
                    cost[h][k+1]=min(cost[h][k+1],abs(grid[h][k+1]-grid[h][k]))
            if vald(h-1,k)  :
                    q.append([h-1,k]) 
                    cost[h-1][k]=min(cost[h-1][k],abs(grid[h-1][k]-grid[h][k]))
            if vald(h,k-1) :
                    q.append([h,k-1])  
                    cost[h][k-1]=min(cost[h][k-1],abs(grid[h][k-1]-grid[h][k]))
            visit[h][k]=False
        return cost[n-1][n-1]
        