// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cach={}
        def dfs(i,tmpsum):
            if i==len(nums):
                if tmpsum==target:return 1
                else:return 0
            # if tmpsum >target:return 0
            if (i,tmpsum) in cach:return cach[(i,tmpsum)]
            cach[(i,tmpsum)]=dfs(i+1,tmpsum+nums[i])+dfs(i+1,tmpsum-nums[i])
            return cach[(i,tmpsum)]
        return dfs(0,0)