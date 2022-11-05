// https://leetcode.com/problems/first-letter-to-appear-twice

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d=defaultdict(int)
        for i in s:
            d[i]+=1
            if d[i]==2:return i
        