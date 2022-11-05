// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative

class Solution:
    def findMaxK(self, l: List[int]) -> int:
        l=sorted(l)
        s=set()
        for i in range(len(l)):
            if l[i] >0:break
            else:s.add(l[i])
        mx=0
        for j in range(i,len(l)):
            if -l[j] in s:mx=max(mx,l[j])
        return  (mx)