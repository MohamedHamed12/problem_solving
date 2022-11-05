// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations

class Solution:
    def countDistinctIntegers(self, l: List[int]) -> int:
        s=set(l)
        ss=list(s)
        tot=len(s)
        for i in ss:
          s.add(int(str(i)[::-1]))
        return len(s)