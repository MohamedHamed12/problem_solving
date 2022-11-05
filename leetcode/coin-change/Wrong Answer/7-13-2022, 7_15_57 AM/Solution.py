// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, l: List[int],c: int) -> int:
        l=sorted(l)
        tot=0
        for i in l[::-1]:
            tot+=c//i
            c=c%i
            if c==0:break
        if c==0:return tot
        else:return tot