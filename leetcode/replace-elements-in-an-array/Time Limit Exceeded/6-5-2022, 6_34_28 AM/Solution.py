// https://leetcode.com/problems/replace-elements-in-an-array

class Solution:
    def arrayChange(self, nums, operations ) :
        for i ,j in operations:
            tem=nums.index(i)
            nums[tem]=j
        return nums
        