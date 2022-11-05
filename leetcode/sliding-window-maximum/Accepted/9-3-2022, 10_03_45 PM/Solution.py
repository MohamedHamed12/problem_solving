// https://leetcode.com/problems/sliding-window-maximum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result=[]
        q=[]
        for i in range(len(nums)):
            while  q and i-q[0]>=k:q.pop(0)
            while q and nums[q[-1]]<nums[i]:q.pop()
            q.append(i)
            if i>=k-1:
                result.append(nums[q[0]])
               
        return result
# print(maxSlidingWindow([1,3,1,2,0,5],3))
       
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
                    
        