// https://leetcode.com/problems/node-with-highest-edge-score

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        l=[0]*(len(edges))
        for i in range(len(edges)) :
            l[edges[i]]+=i
        return l.index(max(l))