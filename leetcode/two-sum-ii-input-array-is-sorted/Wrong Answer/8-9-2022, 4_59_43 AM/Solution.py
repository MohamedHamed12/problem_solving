// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        s=set()
        for i in range(n):
            if numbers[i] in s:continue
            s.add( numbers[i])
            tem=target-numbers[i]
            ind =bisect_right(numbers,tem)
            if ind!=i+1:
                return [i+1,ind]
            # if tem in numbers[i+1:]:return [i+1,i+numbers[i+1:].index(tem)+2]
                       
        
                       