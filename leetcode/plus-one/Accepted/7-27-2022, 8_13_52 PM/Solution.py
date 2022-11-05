// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, l: List[int]) -> List[int]:
        r=[]
        n=len(l)
        tot=0
        for i in range(n):
            tot+=l[i]*(10**(n-i-1))
        tot+=1
        for i in str(tot):
            r.append(int(i))
        return r
        