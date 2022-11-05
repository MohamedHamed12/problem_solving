// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        for i in range(n):
            tem=target-numbers[i]
            if tem in numbers:return [i+1,numbers.index(tem)+1]
                       
        
                       