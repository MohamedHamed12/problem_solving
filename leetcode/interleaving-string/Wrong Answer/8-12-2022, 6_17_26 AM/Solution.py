// https://leetcode.com/problems/interleaving-string

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # def dfs(ind1,ind2,st):
        #     if ind1==len(s1) and ind2==len(s2):
        #         return True if st==s3 else False
        #     for i in range(ind1,len(s1)):
        #         for j in range(ind2,len(s2)):
        #             st+=s1[ind:i] s2
        d=defaultdict(int)     
        for i in s1:d[i]+=1
        for i in s2:d[i]+=1
        for i in s3:d[i]-=1
        if sum(d.values())!=0:return False
        else:return True

        
        
        
        
        
        
        
        # s3=list(s3)
        # for i in s2:
        #     if i in s3:s3.remove(i)
        # if s1=="".join(s3):return True
        # else:return False