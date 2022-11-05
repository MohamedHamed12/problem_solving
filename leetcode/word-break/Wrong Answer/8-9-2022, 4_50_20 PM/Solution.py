// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, dic: List[str]) -> bool:
        n=len(s)
        l=0
        tot=0
        for i in range(n):
            if s[l:i+1] in dic:
                
                tot=i+1
                l=i+1
        if tot==n:return True 
        else:return False
        