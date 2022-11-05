// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        tot=[nums[0]]
        nums.pop(0)
        for  i in range(n-1):
            if nums[i]>tot[-1]:tot.append(nums[i])
            else:tot[bisect.bisect_left(tot,nums[i])]=nums[i]
        return len(tot)
                
        