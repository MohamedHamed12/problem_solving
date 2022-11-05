// https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
#             dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]
        
#             for i in range(1, len(text1) + 1):
#                 for j in range(1, len(text2) + 1):

#                     if text1[i-1] == text2[j-1]:
#                         dp[i][j] = dp[i-1][j-1] + 1
#                     else:
#                         dp[i][j] = max(dp[i-1][j], dp[i][j-1])

#             return dp[-1][-1]
       n=len(a)
       m=len(b)
       dp=[[-float('inf')]*(m+1) for i in range(n+1) ]

       for i in range(n+1):
            for j in range(m+1):
                if i==0 or j==0: dp[i][j]=0
                elif a[i-1] == b[j-1]:dp[i][j]=dp[i-1][j-1]+1
                else:dp[i][j]=max(dp[i-1][j],dp[i][j-1])
       # print(f'Case #1: you can visit at most {dp[-1][-1]} cities.')
       return dp[-1][-1]