// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s=sorted(list(s))
        for i in t:
            if i not in s:return False
        return True