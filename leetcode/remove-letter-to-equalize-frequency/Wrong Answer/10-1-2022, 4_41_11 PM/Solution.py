// https://leetcode.com/problems/remove-letter-to-equalize-frequency

class Solution:
    def equalFrequency(self, word: str) -> bool:
        c=Counter(word)
        c=list(c.values())
        s=list(set(c))
        if len(s)==2:
                if  s[1]-s[0] ==1 and c.count(s[0])==len(c)-1 :return True
                if  s[0]-s[1] ==1 and  c.count(s[1])==len(c)-1:return True
        return False