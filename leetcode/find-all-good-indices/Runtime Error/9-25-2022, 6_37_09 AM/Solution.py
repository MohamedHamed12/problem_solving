// https://leetcode.com/problems/find-all-good-indices

class Solution:
    def goodIndices(self, l: List[int], k: int) -> List[int]:
        n=len(l)
        pfx=[1]*n
        sfx=[1]*n
        tot=[]
        for i in range(1,n):
            if l[i]<=l[i-1]:pfx[i]=pfx[i-1]+1
        for i in range(n-2,-1,-1):
            if l[i]<=l[i+1]:sfx[i]=sfx[i+1]+1
        for i in range(k,n-k+1):
            if pfx[i-1]>=k and sfx[i+1]>=k:tot.append(i)
        print(pfx)
        print(sfx)
        return tot