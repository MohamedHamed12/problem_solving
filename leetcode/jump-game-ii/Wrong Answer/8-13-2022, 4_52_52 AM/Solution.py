// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
            mx =nums[0]
            tot=0
            ind=0
            if mx ==len(nums)-1:return 1
            while ind<len(nums):
             
                tmp=0
                for i in range(ind,ind+mx):
                    
                            tmp=max(nums[i]-(mx-i),tmp)
                ind=ind+mx+1
                tot+=1
                # if mx+ind =len(nums)-1:return tot

            return tot
                