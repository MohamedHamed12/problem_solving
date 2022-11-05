// https://leetcode.com/problems/longest-increasing-path-in-a-matrix

class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        index=[[1,0],[0,1],[-1,0],[0,-1]]
        cache={}
        mx=0
        n=len(mat);m=len(mat[0])
        def valid(i,j):
                if i<n and i>=0 and j>=0 and j< m :return True #and l[i][j]==1 and visit[i][j]
                return  False
        def dfs(i,j,old):
            if not valid(i,j):return 0
            if mat[i][j]<=old: return 0
            if (i,j) in cache:return cache[(i,j)]
            tmp=0
            for u,v in index:
                k=i+u;h=j+v

                tmp=max(tmp,dfs(k,h,mat[i][j]))
            cache[(i,j)]=tmp+1
            return cache[(i,j)]

        for i in range(n):
            for j in range(m):
               mx=max(mx,dfs(i,j,-1))
        return mx