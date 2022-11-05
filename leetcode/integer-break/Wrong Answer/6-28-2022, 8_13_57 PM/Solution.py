// https://leetcode.com/problems/integer-break

class Solution:
    def integerBreak(self, n: int) -> int:
        tot=1
        if n<3:
            return 1
        while n>=3:
            n-=3
            tot*=3
        return tot*n if n>0 else tot
        