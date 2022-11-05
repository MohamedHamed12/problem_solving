// https://leetcode.com/problems/number-of-excellent-pairs

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        tot=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
             
               if bin(nums[i]& nums[j]).count('1')+bin(nums[i] | nums[j]).count('1')>=k:tot+=1
                    
        return tot
        