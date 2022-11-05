// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, l: List[int]) -> List[List[int]]:
        tot=[]
        for i in permutations(l):
           tot.append(list(i))
        return tot