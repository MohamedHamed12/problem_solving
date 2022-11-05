// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
           n=len(nums)  
            
           if n>3: 
              nums[2]+=nums[0]

              for i in range(3,n):
                nums[i]+=max(nums[i-2],nums[i-3])
              return max(nums[n-1],nums[n-2])
           elif n==3:
            
               return max(nums[n-1]+nums[n-3],nums[n-2])
           else:
            return max(nums)
        