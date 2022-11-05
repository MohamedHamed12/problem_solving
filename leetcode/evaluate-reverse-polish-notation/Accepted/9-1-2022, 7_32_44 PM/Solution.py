// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, lst: List[str]) -> int:
        ind=0
        while len(lst)!=1:
            for i in range(ind,len(lst)):
                if not lst[i][-1].isalnum():
                    ind=i
                    break 
            a=int( lst.pop(ind-2))
            b=int( lst.pop(ind-2))
            c=lst.pop(ind-2)
            if c=='+':tem=a+b
            elif c=='-':tem=a-b
            elif c=='*':tem=a*b
            elif c=='/':tem=int(a/b)
            lst.insert(ind-2,str(tem))
            ind-=2
        return lst[-1]