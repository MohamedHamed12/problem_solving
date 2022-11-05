// https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements

class Solution:
    def minimizeTheDifference(self, l: List[List[int]], t: int) -> int:
        s=set([0])
        ans=float('inf')
        for i in l:
            tem=set()
            for j in i:
               
                for k in s:tem.add(k+j)
            s=tem
        for o in s:ans=min(ans,abs(o-t))
        return ans