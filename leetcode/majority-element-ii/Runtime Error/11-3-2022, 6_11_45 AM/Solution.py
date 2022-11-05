// https://leetcode.com/problems/majority-element-ii

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        d=defaultdict(int)
        for i in nums:d[i]+=1
        for i in d:
             if d[i]>=n/3:return i