// https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        n=len(s)
        dp={}
        def dfs(i,j):
            if i>j:return 0
            if i==j:return 0
            if s[i]==s[j]:return dfs(i+1,j-1)
            else:
                dp[(i+1,j)]=dfs(i+1,j)
                dfs(i,j-1)==dfs(i,j-1)
                dp[(i,j)]=min(dp[(i+1,j)],dfs(i,j-1))+1
                return dp[(i,j)]
                
            
        return dfs(0,n-1)