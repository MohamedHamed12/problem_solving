// https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums: List[int]) -> int:
           n=len(nums)  
         
           if n>=4: 
              start=nums[0];end=nums[n-1]
              nums[0]=0;nums[n-1]=0
              nums[2]+=nums[0]

              for i in range(3,n):
                nums[i]+=max(nums[i-2],nums[i-3])
              return max(nums[n-1]+max(start,end),nums[n-2]+start)
           elif n<4:
              return max(nums)
        