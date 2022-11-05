// https://leetcode.com/problems/burst-balloons

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        n=len(nums)
        dp=[[0 for x in range(n)] for x in range(n)]
        for x in range(1,n-1):
            l=1
            for r in range(x,n-1):
                dp[l][r]=max(dp[l][i-1]+nums[l-1]*nums[i]*nums[r+1]+dp[i+1][r] for i in range(l,r+1) )
                l+=1
        return dp[1][n-2]
#         nn=len(nums)
#         nums=[1]+nums+[1]
#         # cache={}
#         @cache
#         def dfs(l,r):
#             if l>=r:return 0
#             tmp=0
#             for cur in range(l+1,r):
#                 prod=nums[cur]*nums[l]*nums[r]
#                 tmp=max(tmp,prod+dfs(l,cur)+dfs(cur,r))
                
#             return tmp
#         return dfs(0,len(nums) - 1)


#         orig_size = len(nums)
#         nums = [1] + nums + [1]
        
#         @cache
#         def dfs(left, right):
#             if left >= right:
#                 return 0
            
#             ret = 0
            
#             for last in range(left + 1, right):
#                 # remainder: we want to burst all the way to the left/right
#                 prod = nums[left] * nums[last] * nums[right]
#                 # note, here k is always skipped in the recursive calls below 
#                 ret = max(ret, prod + dfs(left, last) + dfs(last, right))
            
#             return ret
         
#         # we never want to pop the virtual 1s so we start at i + 1 in the loop
#         return dfs(0, len(nums) - 1)