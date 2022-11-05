// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(i.lower() for i in s if i.isalpha() )
        
        if list(s)==list(s)[::-1]:return True 
        else:return False