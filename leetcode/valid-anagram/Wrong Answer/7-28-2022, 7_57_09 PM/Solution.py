// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(list(s));t=sorted(list(s))
        if s==t:return True 
        return False
        