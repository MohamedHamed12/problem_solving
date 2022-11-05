// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        l=[0]*(n+2)
        for i in range(n):
            l[i+1]+=1
            l[i+2]+=1
        return l[n]
            
            
        