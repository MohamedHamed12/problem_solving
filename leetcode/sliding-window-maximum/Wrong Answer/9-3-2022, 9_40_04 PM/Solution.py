// https://leetcode.com/problems/sliding-window-maximum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result=[]
        q=[]
        for i in range(len(nums)):
            if len(q)>k:q.pop(0)
            while q and q[-1]<nums[i]:q.pop()
            q.append(nums[i])
            if i>=k-1:
                result.append(q[0])
        return result
       
#         if not nums or k == 0:
#             return []

#         tmp=sorted(nums[:k])
#         l=[tmp[-1]]
#         for i in range(k,len(nums)):
#               ind=bisect_right(tmp,nums[i-k])
#               del tmp[ind-1]
#               insort(tmp,nums[i])
#               l.append(tmp[-1])
#         return l
                    
        