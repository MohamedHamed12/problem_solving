// https://leetcode.com/problems/delete-operation-for-two-strings

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
       
        n1=len(word1);     n2=len(word2)
        dp=[[0]*(n2+1) for _ in range(n1+1)]
        for i in range(n1+1):
            for j in range(n2+1):
                if i==0 or j==0:continue
                if word1[i-1]==word2[j-1]:dp[i][j]=dp[i-1][j-1]+1
                else:dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        r=n1+n2-2*dp[-1][-1]
        return r
#         memo={}
#         def rec(i,j):
#             if i==n1 :return n2-j 
#             if j==n2:return n1-i
#             if (i,j) in memo:return memo[(i,j)]
            
#             if word1[i]==word2[j]:  ret=rec(i+1,j+1)
#             else: ret=min(rec(i+1,j),rec(i,j+1))+1
               
#             memo[(i,j)]=ret
#             return ret
#         return rec(0,0)
        