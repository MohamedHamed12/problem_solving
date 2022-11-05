// https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome

class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        dp=[[0]*(n+1) for i in range(n+1)]
        r=s[::-1]
        for i in range(n+1):
            for j in range(n+1):
                if i==0 or j==0:continue 
                if s[i-1]==r[j-1]:dp[i][j]=dp[i-1][j-1]
                else:dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1
        return dp[-1][-1]
                
#         dp={}
#         def dfs(i,j):
#             if i>=j:return 0
#             if  (i,j) in dp:return dp[(i,j)]
#             if s[i]==s[j]:return dfs(i+1,j-1)
#             else:
#                 dp[(i+1,j)]=dfs(i+1,j)
#                 dfs(i,j-1)==dfs(i,j-1)
#                 dp[(i,j)]=min(dp[(i+1,j)],dfs(i,j-1))+1
#                 return dp[(i,j)]
                
            
#         return dfs(0,n-1)
    
    