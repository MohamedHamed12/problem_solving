// https://leetcode.com/problems/last-stone-weight

class Solution:
    def lastStoneWeight(self, l: List[int]) -> int:
        l=sorted(l)

        while len(l)>1:
            tem1=l.pop(-1)
            tem2=l.pop(-1)
            if tem1!=tem2:insort(l,abs(tem1-tem2))
        return l[-1]
