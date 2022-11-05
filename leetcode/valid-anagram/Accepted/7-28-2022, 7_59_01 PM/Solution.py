// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s=sorted(list(s));t=sorted(list(t))
        # if s==t:return True 
        # return False
        if len(t) != len(s): return False
        s_counter = Counter(s)
        t_counter = Counter(t)     
        
        for char, occurrences in t_counter.items():
            if char not in s_counter: return False
            if s_counter[char] != occurrences: return False
        
        return True
        