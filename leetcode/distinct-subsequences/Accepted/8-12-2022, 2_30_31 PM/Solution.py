// https://leetcode.com/problems/distinct-subsequences

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache={}
        def dfs(i,j):
            if j==len(t):return 1
            if i==len(s):return 0
        
            if (i,j) in cache:return cache[(i,j)]
            tmp=0
            tmp+=dfs(i+1,j) 
            if s[i]==t[j]:
                tmp+=dfs(i+1,j+1) 
            cache[(i,j)]=tmp
            return tmp
        
        
        return dfs(0,0)