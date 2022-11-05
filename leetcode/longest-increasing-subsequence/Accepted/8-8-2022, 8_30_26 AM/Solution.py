// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mx=0
        n=len(nums)
        dp=[0 for i in range(n)]
        for i in range(n):
            cur=nums[i]
            tem=1
            for j in range(i-1,-1,-1):
                if  cur >nums[j]:
                    tem=max(dp[j]+1,tem) 
            dp[i]=tem
            
            
            
            
        return max(dp)
#         n=len(nums)
#         tot=[nums[0]]
#         nums.pop(0)
#         for  i in range(n-1):
#             if nums[i]>tot[-1]:tot.append(nums[i])
#             else:tot[bisect.bisect_left(tot,nums[i])]=nums[i]
#         return len(tot)
                
        