// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:return 1
        if n==2:return 2
        l=[0]*(n)
        
        l[1]=2
        l[0]=1
        for i in range(2,n):
            l[i]=l[i-1]+l[i-2]
          
        return l[n-1]
            
            
        