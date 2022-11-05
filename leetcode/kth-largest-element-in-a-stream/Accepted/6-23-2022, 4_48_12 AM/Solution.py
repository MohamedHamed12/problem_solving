// https://leetcode.com/problems/kth-largest-element-in-a-stream

import bisect
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
         self.k=k    
         self.l=sorted(nums)
    def add(self, val: int) -> int:     
        bisect.insort(self.l,val)
        return self.l[-self.k]
      
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)