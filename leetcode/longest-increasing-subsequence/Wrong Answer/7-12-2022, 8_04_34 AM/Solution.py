// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mx=-1
       
        n=len(nums)
        if n==1:return nums[0]
        l=[1]*n
        for i in range(1,n):
            for j in range(0,i):
                 if nums[i]>nums[j]:
                    l[i]=max(l[i],l[j]+1)
            mx=max(mx,l[i])
            
        return mx