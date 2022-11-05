// https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, l: List[int]) -> List[List[int]]:
        tot=[]
        for i in [itertools.combinations(l,_) for _ in range(len(l)+1)]:
            for j in i:
              if list(j) not in tot: tot.append(list(j))
        # print(tot)
        return tot
        