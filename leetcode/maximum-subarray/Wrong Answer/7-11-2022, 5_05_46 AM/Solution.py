// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tot=0;n=len(nums)
        mxsum=0

        for i in range(n):
             tot+=nums[i]
             nums[i]=tot
             for j in range(i):
                    if nums[i]-nums[j]>mxsum:mxsum= nums[i]-nums[j]
            
           
        return mxsum          
        