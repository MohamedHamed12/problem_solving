// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
              c=sorted(Counter(nums).items(),key=lambda x: x[1],reverse=True)
              return [c[i][0] for i in range(k)]     