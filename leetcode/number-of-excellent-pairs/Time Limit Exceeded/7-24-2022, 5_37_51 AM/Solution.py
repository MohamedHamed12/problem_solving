// https://leetcode.com/problems/number-of-excellent-pairs

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        tot=0
        nums=list(set(nums))
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
             
               if bin(nums[i]& nums[j]).count('1')+bin(nums[i] | nums[j]).count('1')>=k:
                  if nums[i]==nums[j]:tot+=1
                  else:tot+=2
                  
                    
        return tot
        