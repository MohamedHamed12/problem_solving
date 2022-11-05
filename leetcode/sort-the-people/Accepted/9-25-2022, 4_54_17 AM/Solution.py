// https://leetcode.com/problems/sort-the-people

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l=zip(heights, names)
        l=sorted(l,reverse=True)
        return [j  for i,j in l]