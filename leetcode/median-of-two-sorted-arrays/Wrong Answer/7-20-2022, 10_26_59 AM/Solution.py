// https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, a1: List[int], a2: List[int]) -> float:
        return((sum(a1)+sum(a2))/(len(a1)+len(a2)))
        