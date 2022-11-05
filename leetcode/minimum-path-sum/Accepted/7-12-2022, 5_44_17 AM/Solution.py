// https://leetcode.com/problems/minimum-path-sum

class Solution:
   def minPathSum(self, grid) :
        n=len(grid);m=len(grid[0])
        cost=[[float('inf')]*m for i in range(n)]
        visit=[[True]*m for i in range(n)]
        def vaild(i,j):
            if i in range(n) and  j in range(m):return True
            else: return False
        cost[0][0]=grid[0][0]
        for i in range(n):
            for j in range(m):
               if vaild(i+1,j):cost[i+1][j]=min(cost[i+1][j],cost[i][j]+grid[i+1][j])
               if vaild(i,j+1):cost[i][j+1]=min(cost[i][j+1],cost[i][j]+grid[i][j+1])
        return cost[n-1][m-1]
