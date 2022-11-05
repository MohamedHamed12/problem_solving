// https://leetcode.com/problems/mirror-reflection

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        L = lcm(p,q)
        if (L%(2*p))==0:return 0
        else:
            if (L//q)%2==1:return 1
            else:return 2 
