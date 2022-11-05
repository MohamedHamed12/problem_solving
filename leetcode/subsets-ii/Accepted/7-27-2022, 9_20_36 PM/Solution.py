// https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, l: List[int]) -> List[List[int]]:
        tot=[]
        for i in [itertools.combinations(l,_) for _ in range(len(l)+1)]:
            for j in i:
                m=sorted(list(j))
                if  m not in tot : tot.append(m)
        # print(tot)
        return sorted(tot)
        