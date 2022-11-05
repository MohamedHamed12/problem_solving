// https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        tot=0
        n=0
        for  i in nums:
            if i%3==0:tot+=i;n+=1
        return tot/n
        