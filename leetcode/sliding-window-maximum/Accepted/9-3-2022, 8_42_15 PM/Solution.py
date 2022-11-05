// https://leetcode.com/problems/sliding-window-maximum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       
        

        tmp=sorted(nums[:k])
        l=[tmp[-1]]
        for i in range(k,len(nums)):
              ind=bisect_right(tmp,nums[i-k])
              del tmp[ind-1]
              insort(tmp,nums[i])
              l.append(tmp[-1])
        return l
                    
        