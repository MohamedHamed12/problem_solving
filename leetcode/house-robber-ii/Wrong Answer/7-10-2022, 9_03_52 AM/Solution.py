// https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums: List[int]) -> int:
           n=len(nums)  
           start=nums[0]
           nums[0]=0
           if n>3: 
              nums[2]+=nums[0]

              for i in range(3,n):
                nums[i]+=max(nums[i-2],nums[i-3])
              return max(nums[n-1],nums[n-2]+start)
           elif n<4:
              return max(nums)
        