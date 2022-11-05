// https://leetcode.com/problems/construct-smallest-number-from-di-string

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        l=groupby(pattern)

        ind=1
        lst=[str(i+1) for i in  range(len(pattern)+1)]
       
        for i,j in l:
            j=len(list(j))
            if i=='D':
                if ind==1:

                    lst=lst[:ind-1]+lst[ind-1:ind+j][::-1]+lst[ind+j:]
                elif j==1:
                    lst=lst[:ind-1]+lst[ind-1:ind+j][::-1]+lst[ind+j:]
                else:lst=lst[:ind-1]+lst[ind-1:ind+j][::-1]+lst[ind+j:]
            ind+=j
                
        return "".join(lst)