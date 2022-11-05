// https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, lst: List[int]) -> List[int]:
        tot=[0]*len(lst)
        stack=[]
        for i in range(len(lst)):
            while stack and stack[-1][0]<lst[i]:
                cur ,ind=stack.pop()
                tot[ind]=i-ind
            stack.append((lst[i],i))
        
        while stack:
                cur ,ind=stack.pop()
                tot[ind]=0
        return tot