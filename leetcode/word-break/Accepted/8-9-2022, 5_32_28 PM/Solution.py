// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, dic: List[str]) -> bool:
         n=len(s)
         dp=[False]*(n+1)
         dp[-1]=True
         for i in range(n-1,-1,-1):
                for w in dic:
                    if i+len(w)<=n and s[i:i+len(w)]==w :dp[i]=dp[i+len(w)]
                    if dp[i]:break
                
         return dp[0]
        
        
        
        
        
        
        
        
        
        #         n=len(s)
#         l=0
#         tot=0
#         for i in range(n):
#             if s[l:i+1] in dic:
                
#                 tot=i+1
#                 l=i+1
#         if tot==n:return True 
#         else:return False
        