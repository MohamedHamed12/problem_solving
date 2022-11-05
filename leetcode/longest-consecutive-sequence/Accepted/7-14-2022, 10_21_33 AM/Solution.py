// https://leetcode.com/problems/longest-consecutive-sequence

class Solution(object):
    def longestConsecutive(self, nums):
        nums=sorted(set(nums));n=len(nums)
        if n==1:return 1
        h=tot=0
        for i in range(1,n):
            
                if nums[i]-nums[i-1]>1:
                    tot=max(i-h,tot)
                    h=i
            
            
        tot=max(n-h,tot)
        return tot