// https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums=deque(nums)
        x=nums[0]
        n=len(nums)
        for i in range(1,n):
            x^=nums[i]
        return x
        # d=Counter(nums)
        # for i in d:
        #     if d[i]==1:
        #      return i