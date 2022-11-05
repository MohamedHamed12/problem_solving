// https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c=Counter(s[0])
        n=len(s)
        mx=1
        l=0 ;r=0
        while l<n and r<n:
            rem=(r-l+1)-max(c.values())
            if rem<=k:
                mx=max(mx,r-l+1)
                r+=1
                if r<n:c[s[r]]+=1
                
            else:
                l+=1
                if l<n:c[s[l]]+=1
        return mx
            