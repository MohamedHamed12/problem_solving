// https://leetcode.com/problems/largest-local-values-in-a-matrix

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)

        # l=[[0]*(n-3+1)for i in range(n-3+1)]
        d=defaultdict(int)
        for i in range(n-2):
            for j in range(n-2):
                d[((i,i+2),(j,j+2))]=0
        for i in range(n):
            for j in range(n):
                tmp=grid[i][j]
                for (h,k),(o,p) in d:
                    if i>=h and i<=k and j>=o and p>=j:d[((h,k),(o,p))]=max(d[((h,k),(o,p))],tmp) 
        l=list(d.values())
        f=[ l[u:u+n-2] for u in range(0,len(d),n-2)]
        return f