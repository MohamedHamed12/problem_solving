// https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, a1: List[int], a2: List[int]) -> float:
        a1=list(set(a1+a2))
        a1=sorted(a1)
        if len(a1)%2==0:
            ind=-1+len(a1)//2
            return (a1[ind]+a1[ind+1])/2
        else:
            return a1[len(a1)//2]