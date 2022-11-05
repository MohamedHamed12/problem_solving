// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        d=defaultdict(int)
        for i in nums:d[i]+=1
        for i in d:
             if d[i]>=n/2:return i