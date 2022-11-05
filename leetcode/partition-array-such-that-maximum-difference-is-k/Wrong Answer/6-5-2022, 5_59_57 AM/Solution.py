// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k

class Solution:
     def partitionArray(self, nums,k ) :
        nums=sorted(nums)
        j=0
        tot=0
        for i in range(len(nums)):
            if nums[j]-nums[i]<=k:
                pass
            else:
                j=i
                tot+=1
        return tot