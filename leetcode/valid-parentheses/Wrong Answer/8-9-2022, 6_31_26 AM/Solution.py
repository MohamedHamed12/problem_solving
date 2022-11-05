// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':l.append(i)
            elif (i==')' and l[-1]=='(' )or i==']' and l[-1]=='[' or i=='}' and l[-1]=='{':

                l.pop()
            else:return False
        return True
        