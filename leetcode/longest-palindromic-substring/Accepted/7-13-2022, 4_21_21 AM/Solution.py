// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s);mx=""
        for i in range(n):
            m1=self.check(s,i,i);mx=m1 if len(m1)> len(mx) else mx
            m2=self.check(s,i,i+1);mx=m2 if len(m2)> len(mx)  else mx
            # mx=max(m1,m2,mx)
        return mx
    def check(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]