// https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c=Counter(s)
        m=max(c.values())
        return min(len(s),m+k)