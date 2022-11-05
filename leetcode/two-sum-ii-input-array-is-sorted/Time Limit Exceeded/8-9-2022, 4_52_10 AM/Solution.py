// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        for i in range(n):
            tem=target-numbers[i]
            if tem in numbers[i+1:]:return [i+1,i+numbers[i+1:].index(tem)+2]
                       
        
                       