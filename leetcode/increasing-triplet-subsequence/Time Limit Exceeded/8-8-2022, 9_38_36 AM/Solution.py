// https://leetcode.com/problems/increasing-triplet-subsequence

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[0 for i in range(n)]
        for i in range(n):
            cur =nums[i]
            tem=1
            for j in range(i-1,-1,-1):
                if cur>nums[j]:tem=max(tem,dp[j]+1)
            dp[i]=tem
            if tem>=3:return True
        return False
        
        
                