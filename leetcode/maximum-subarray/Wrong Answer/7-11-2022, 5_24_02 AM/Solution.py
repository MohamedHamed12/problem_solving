// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums.insert(0,0)
        tot=0;n=len(nums)
        if n==2:return nums[1]
        mxsum=-maxsize

        for i in range(n):
             tot+=nums[i]
             nums[i]=tot
             if i>0:
                m=min(nums[:i])
                if nums[i]-m>mxsum:mxsum= nums[i]-m
            
           
        return max(nums)-min(nums)
        