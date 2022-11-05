// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot=1
        t=1
        z=0
        for i in nums:
            t*=i
            if i!=0:tot*=i
            if i==0:z+=1
            if z==2:
                return [0]*len(nums)
        tem=[]
        
        for i in nums:
            
            if i!=0:tem.append (t//i )
            else:tem.append(tot)
        return tem