// https://leetcode.com/problems/combination-sum-ii

class Solution:
    def combinationSum2(self, l: List[int], target: int) -> List[List[int]]:
            tot=[]
            for i in [itertools.combinations(l,_) for _ in range(len(l)+1)]:
                for j in i:
                    if sum(j)==target:
                        m=sorted(list(j))
                        if  m not in tot and sum: tot.append(m)
            # print(tot)
            return sorted(tot)
        