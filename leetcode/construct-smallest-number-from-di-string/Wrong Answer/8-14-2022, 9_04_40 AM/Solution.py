// https://leetcode.com/problems/construct-smallest-number-from-di-string

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        l=groupby(pattern)

        ind=1
        lst=[]
        tmp=[]
        for i,j in l:
            j=len(list(j))
            if i=='I':
                for i in range(ind,ind+j):lst.append(i )
                ind+=j
                lst+=tmp[::-1]
                tmp.clear()
            elif i=='D':
                for i in  range(ind,ind+j):tmp.append(i )
                ind+=j
        tmp.append(ind)
        lst+=tmp[::-1]
        return lst