// https://leetcode.com/problems/count-of-smaller-numbers-after-self

class Solution:
    # def countSmaller(self, nums: List[int]) -> List[int]:
    #         tot=[]
    #         snum=sorted((nums))
    #         for i in range(len(nums)):
    #             tem=bisect_left(snum,nums[i])
    #             tot.append(tem)
    #             del(snum[tem])
    #         return (tot)
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr, ans = sorted(nums), []     #   <-- 1)
        
        for num in nums:
            i = bisect_left(arr,num)    #   <-- 2a)
            ans.append(i)               #   <-- 2b)
            del arr[i]                  #   <-- 2c)
            
        return ans                      #   <-- 3)