// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        for i in range(1,n):
            if nums[i-1]==0:return False
            nums[i]=max(nums[i-1]-1,nums[i])
        return True 