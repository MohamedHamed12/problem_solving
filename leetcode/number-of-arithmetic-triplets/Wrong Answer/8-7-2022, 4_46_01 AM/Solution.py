// https://leetcode.com/problems/number-of-arithmetic-triplets

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
      
        tot=0
        s2=set()
        s=set(nums)

        for i in nums:
            if i not in s2 and  i+diff and i+2*diff in s:
                tot+=1
                s2.add(i)
                s2.add( i+diff )
                s2.add(i+2*diff)

        return tot