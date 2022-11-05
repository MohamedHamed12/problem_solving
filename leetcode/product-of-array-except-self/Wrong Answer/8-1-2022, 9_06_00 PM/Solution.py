// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot=1
        for i in nums:
            if i!=0:tot*=i
        tem=[]
        for i in nums:
            
            if i!=0:tem.append (tot//i )
            else:tem.append(tot)
        return tem