// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, l: List[int]) -> int:
        res=max(l)
        mx=mn=1
        for i in l:
            temx=mx;temn=mn
            mx=max(i,temx*i,temn*i)
            mn=max(i,temx*i,temn*i)
            res=max(res,mx)
        
        return res
        
        
        
        
        
        
        
        
        
        
        
#         res = max(nums)
#         curMin=curMax = 1
#         for n in nums:

#             tmpx = curMax * n
#             temn=  curMin* n
#             curMax = max(tmpx,temn, n)
#             curMin = min(tmpx, temn, n)
#             res = max(res, curMax)
#         return res
            #         a=len(l)
#         mx=-float('inf')
#         l.append(0)
#         for j in range(a,-1,-1):
#             t-=l[j]
#             mx=max(mx,t)

#             for i in range(j):

#                 t-=l[i]
#                 mx=max(mx,t)
#         return mx
