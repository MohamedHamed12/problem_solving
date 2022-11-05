// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        tmp=0
        q=[]
        for i in range(len(h)):
            if q and q[-1] <=h[i]:
                q.append(h[i])
            else:
                ind=1
                while q and  q[-1]>h[i]:
                    tmp=max(tmp,q.pop()*ind)
                    ind+=1
                q.append(h[i])
        ind=1
        while q:
            tmp=max(tmp,q.pop()*ind)
            ind+=1
        return tmp