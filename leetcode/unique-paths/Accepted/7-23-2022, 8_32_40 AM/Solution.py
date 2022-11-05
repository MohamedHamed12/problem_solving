// https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        l=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:l[i][j]=1
                else:
                    l[i][j]=l[i-1][j]+l[i][j-1]
                
        return l[-1][-1]