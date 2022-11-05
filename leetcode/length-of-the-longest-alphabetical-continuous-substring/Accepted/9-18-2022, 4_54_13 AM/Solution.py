// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        tot=1
        tmp=1
        for i in range(1,len(s)):
            if ord(s[i])-ord(s[i-1])==1:
                tmp+=1
                tot=max(tmp,tot)
            else:tmp=1
        return tot
        