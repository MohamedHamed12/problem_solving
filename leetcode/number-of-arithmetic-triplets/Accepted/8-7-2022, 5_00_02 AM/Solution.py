// https://leetcode.com/problems/number-of-arithmetic-triplets

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
      
        tot=0
        s2=set()
        s=set(nums)

        for i in nums:
       
            if   i+diff in s and i+2*diff in s:
                tot+=1
                
        return tot