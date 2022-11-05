// https://leetcode.com/problems/construct-smallest-number-from-di-string

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        l=groupby(pattern)

        ind=1
        lst=[str(i+1) for i in  range(len(pattern)+1)]
        # tmp=[]
        for i,j in l:
            j=len(list(j))
            # if i=='I':
            #     for i in range(ind,ind+j):lst.append(str(i))
            #     ind+=j
            #     lst+=tmp[::-1]
            #     tmp.clear()
            if i=='D':
                if ind==1:

                    lst=lst[:ind-1]+lst[ind-1:ind+j][::-1]+lst[ind+j:]
                elif j==1:
                    lst=lst[:ind-1]+lst[ind-1:ind+j][::-1]+lst[ind+j:]
                else:lst=lst[:ind-1]+lst[ind-1:ind+j][::-1]+lst[ind+j:]
            ind+=j
                # for i in  range(ind,ind+j):tmp.append(str(i) )
                # ind+=j
        # tmp.append(str(ind))
        # lst+=tmp[::-1]
        return "".join(lst)