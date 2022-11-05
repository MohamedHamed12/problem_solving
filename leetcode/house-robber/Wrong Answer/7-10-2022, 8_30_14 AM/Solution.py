// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
          n=len(nums)  
          for i in range(2,n):
              nums[i]+=nums[i-2]
          return max(nums[n-1],nums[n-2])
        