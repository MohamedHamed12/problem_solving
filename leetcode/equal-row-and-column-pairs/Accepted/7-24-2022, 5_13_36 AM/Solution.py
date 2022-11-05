// https://leetcode.com/problems/equal-row-and-column-pairs

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        tot=0
        n=len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i]==[grid[x][j] for x in range(n)]:tot+=1
        return tot