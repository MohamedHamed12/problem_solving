// https://leetcode.com/problems/largest-local-values-in-a-matrix

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)

        l=[[0]*(n-3+1)for i in range(n-3+1)]
        
        for i in range(len(l)):
            for j in range(len(l)):
                tmp=-maxsize
                for h in range(i,i+3):
                    for k in range(j,j+3):
                        tmp=max(tmp,grid[h][k])

                l[i][j]=tmp
        return l
                