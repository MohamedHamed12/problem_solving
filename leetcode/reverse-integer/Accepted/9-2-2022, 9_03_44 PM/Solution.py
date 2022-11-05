// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        s=1 if x<0 else 0
        x=int(str(abs(x))[::-1]) 
        x=x*-1 if s else x
        return x if x<=(2**31)-1 and x>=-2**31 else 0
