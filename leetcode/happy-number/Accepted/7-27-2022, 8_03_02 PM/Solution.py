// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
            tem=collections.deque()
            while n!=1:
                tot=0
                for i in str(n):
                    tot+=int(i)**2
                if tot in tem: return False
                tem.append(n)
                n=tot
            if n==1: return True
