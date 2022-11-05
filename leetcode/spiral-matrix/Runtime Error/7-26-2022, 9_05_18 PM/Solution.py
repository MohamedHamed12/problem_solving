// https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        tot=[]
        while m:
             if m:
                for i in m.pop(0):
                  tot.append(i)
             
             if m:
                for i in range(len(m)):
                  tot.append(m[i].pop())
             if m:
                for i in m.pop()[::-1]:
                  tot.append(i)
             if m:
                for i in range(len(m)-1,-1,-1):
                  if m[i]:tot.append(m[i].pop(0))
        return tot 
            