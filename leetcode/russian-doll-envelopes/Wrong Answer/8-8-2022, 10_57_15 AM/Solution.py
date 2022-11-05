// https://leetcode.com/problems/russian-doll-envelopes

class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        n=len(e)
        tot=0
        a=0;b=0
        e=sorted(e,key=lambda x:x[0])
        for u,v in e:
            if u>a  and v>b:
                a,b=u,v
                tot+=1
        return tot