// https://leetcode.com/problems/subsets

from itertools import combinations, permutations, combinations
class Solution:
    def subsets(self, l: List[int]) -> List[List[int]]:
       
       
        combs = (((combinations(l, r)) for r in range(0, len(l) + 1)))
        tot = []
        for i in combs:
            for j in i:
                tot.append(list(j))

        return tot