// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        tot=[1]*n
        l=1;r=1
        for i in range(1,n):
            l*=nums[i-1]
            tot[i]=l
        for i in range(n-2,-1,-1):
            r*=nums[i+1]
            tot[i]*=r
        return tot
#         tot=1
#         t=1
#         z=0
#         for i in nums:
#             t*=i
#             if i!=0:tot*=i
#             if i==0:z+=1
#             if z==2:
#                 return [0]*len(nums)
#         tem=[]
        
#         for i in nums:
            
#             if i!=0:tem.append (t//i )
#             else:tem.append(tot)
#         return tem