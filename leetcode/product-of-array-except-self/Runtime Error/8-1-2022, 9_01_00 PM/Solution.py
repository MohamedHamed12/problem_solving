// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot=1
        for i in nums:tot*=i
        return [tot//i for i in nums]