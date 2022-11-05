// https://leetcode.com/problems/count-of-smaller-numbers-after-self

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
            tot=[]
            snum=sorted((nums))
            for i in range(len(nums)):
                tem=bisect_left(snum,nums[i])
                tot.append(tem)
                del(snum[tem])
            return (tot)