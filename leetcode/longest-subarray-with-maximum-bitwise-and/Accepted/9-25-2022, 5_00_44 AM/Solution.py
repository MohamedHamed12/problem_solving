// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx=max(nums)
        tmp=0
        for i ,j in groupby(nums):
            if i==mx:tmp=max(tmp,len(list(j)))
        return tmp
        