// https://leetcode.com/problems/kth-largest-element-in-an-array

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         return sorted(nums,reverse=True)[k-1]
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # build the min heap (use -n so that the largest will be on top)
        # nums: [3,2,1,5,6,4] --> heap: [-6,-5,-4,-3,-2,-1]
        for n in nums:
            heapq.heappush(heap, -n)
        
        # pop k times to get the kth largest element
        for i in range(k):
            cur = heapq.heappop(heap)
        
        # remember to turn element back to positive by adding "-"
        return -cur