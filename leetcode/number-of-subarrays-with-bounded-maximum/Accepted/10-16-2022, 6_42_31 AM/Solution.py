// https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
       end=start=-1
     
       tot=0
       for i,ele in enumerate (nums):
           if ele>right:
               end=start=i
               continue
           elif ele>=left:  end=i
             
           tot+=end-start
       return tot
             