// https://leetcode.com/problems/replace-elements-in-an-array

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
            replacements = {}
            for x, y in reversed(operations):
                # replacements[x] = replacements.get(y, y)
                replacements[x]= replacements[y] if y in replacements else y
            for idx, val in enumerate(nums):
                if val in replacements:
                    nums[idx] = replacements[val]
            return nums