// https://leetcode.com/problems/interleaving-string

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # def dfs(ind1,ind2,st):
        #     if ind1==len(s1) and ind2==len(s2):
        #         return True if st==s3 else False
        #     for i in range(ind1,len(s1)):
        #         for j in range(ind2,len(s2)):
        #             if dfs(i,j,st+s1[ind1:i] +s2[ind2:j]):return True
                    
                    
        def dfs(i,h,k):
            if h>len(s1) or k>len(s2):return False
            if i==len(s3):
                if h==len(s1) and k==len(s2):return True
                return False
            if h<len(s1) and k<len(s2) and s3[i]==s1[h] ==s2[k]:
                return dfs(i+1,h+1,k) or dfs(i+1,h,k+1)
                
            if h<len(s1) and s3[i]==s1[h]:return dfs(i+1,h+1,k)
                
            elif k<len(s2) and s3[i]==s2[k]:return dfs(i+1,h,k+1)
            else:return False
                    
        return dfs(0,0,0) 
                    
        # d=defaultdict(int)     
        # for i in s1:d[i]+=1
        # for i in s2:d[i]+=1
        # for i in s3:d[i]-=1
        # if sum(d.values())!=0:return False
        # else:return True
#         h=0;k=0
#         for i in s3 :
#             if k<len(s2) and i==s2[k]:k+=1 
#             elif h<len(s1) and i==s1[h]:h+=1
#             else:
#                 if h==len(s1) and k==len(s2) and h+k==len(s3):return True
#                 return False
#         if h==len(s1) and k==len(s2) and h+k==len(s3):return True

        
        
        
        
        
        
        # s3=list(s3)
        # for i in s2:
        #     if i in s3:s3.remove(i)
        # if s1=="".join(s3):return True
        # else:return False