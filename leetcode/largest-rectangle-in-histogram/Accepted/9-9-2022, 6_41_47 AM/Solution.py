// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        tmp=0
        h.append(0)
        q=[]
        for i in range(len(h)):
            while  q and h[q[-1]] >h[i]:
              
                
                    x=q.pop()
                    w=i if not q else i-q[-1]-1
                    tmp=max(tmp,w*h[x])
            q.append(i)
    
        return tmp