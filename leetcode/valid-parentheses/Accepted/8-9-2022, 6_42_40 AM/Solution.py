// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        dic = {"(" : ")" ,"[" :"]","{" :"}"}
        for i in s:
            if i in dic:l.append(i)
            elif len(l)>0 and i==dic[l[-1]]:l.pop()
            else:return False
        if l:return False
        return True
    
    
           # if i=='(' or i=='{' or i=='[':l.append(i)
            # elif( l) and ( ((i==')' and l[-1]=='(' ))or (i==']' and l[-1]=='[') or (i=='}' and l[-1]=='{')):