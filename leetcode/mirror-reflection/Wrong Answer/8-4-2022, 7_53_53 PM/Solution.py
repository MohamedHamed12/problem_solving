// https://leetcode.com/problems/mirror-reflection

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if q==0:return 0
        if p%2==0:return 2
        else:return 1
        