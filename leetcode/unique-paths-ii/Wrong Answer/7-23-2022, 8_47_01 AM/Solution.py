// https://leetcode.com/problems/unique-paths-ii

class Solution:
    def uniquePathsWithObstacles(self, obs: List[List[int]]) -> int:
        m=len(obs);n=len(obs[0])
        l=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:l[i][j]=1
                else:
                    l[i][j]=l[i-1][j]+l[i][j-1]
                
                if obs[i][j]==1:
                   l[i][j]=0
        return l[-1][-1]