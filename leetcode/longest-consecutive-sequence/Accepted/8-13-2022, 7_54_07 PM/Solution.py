// https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, l: List[int]) -> int:
        l=sorted(l)
        if not l:return 0
        tmp=l[0]
        tot=1
        mx=0
        for i in range(1,len(l)):
            if l[i]==tmp :continue
            if l[i]==tmp+1:tot+=1
            else:
                mx=max(mx,tot)
                tot=1
                
            tmp=l[i]
        mx=max(mx,tot)
        return mx