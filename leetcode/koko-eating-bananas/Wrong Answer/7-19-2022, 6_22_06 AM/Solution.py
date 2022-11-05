// https://leetcode.com/problems/koko-eating-bananas

class Solution(object):
    def minEatingSpeed(self, piles, h):
        n=len(piles)
        l=1 ;r=sum(piles)
        while r-l>1:
            m=(r+l)//2
            cost=0
            for i in range(n):cost+=math.ceil(piles[i]/m)
            if cost<h:r=m
            else:l=m
        return r
        