// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes

class Solution:
    def findSmallestSetOfVertices(self, n: int, lst: List[List[int]]) -> List[int]:
        l=[0]*n
        tot=[]
        for u,v in lst :
            l[v]+=1
        for i in range(n):
            if l[i]==0:tot.append(i)
        return tot