// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        tmp=nums[0]
        mx=0
        tot=0
        for i in range(len(nums)):
            if i+tmp==len(nums)-1:return 1+tot
            mx=max(mx,nums[i]-tmp)
            if tmp==0:
                tmp=mx
                mx=0
                tot+=1
                
            
            tmp-=1
        return tot
            #             mx =nums[0]
#             tot=0
#             ind=0
#             if len(nums)==1:return 0
#             # if mx ==len(nums)-1:return 1
#             while ind+mx<len(nums)-1:
             
#                 tmp=0
#                 for i in range(ind,ind+mx):
                    
#                             tmp=max(nums[i]-(mx-i),tmp)
#                 ind=ind+mx+1
#                 tot+=1
#                 # if mx+ind =len(nums)-1:return tot

#             return tot
                