// https://leetcode.com/problems/count-of-smaller-numbers-after-self

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
            tot=[]
            snum=sorted(nums)
            for i in range(len(nums)):
                tem=bisect_right(snum,nums[i])
                tot.append(tem-1)
                del(snum[tem-1])
            return (tot)