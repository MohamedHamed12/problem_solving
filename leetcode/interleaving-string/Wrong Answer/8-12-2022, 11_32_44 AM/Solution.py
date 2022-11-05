// https://leetcode.com/problems/interleaving-string

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    
             n,m=len(s1),len(s2)
             if len(s3)!=n+m:return False
             if len(s3)==1:
                    return s3==s1 or s3==s2
             dp=[[False]*(m+1) for i in range(n+1)]
             dp[0][0]=True
             for i in range(1,n+1):
                    dp[i][0]= dp[i-1][0] and s1[i-1]
                    
             for j in range(1,m+1):
                    dp[0][j]= dp[0][j-1] and s2[j-1]
             for i in range(1,n+1):
                for j in range(1,m+1):
                    dp[i][j]=(dp[i][j-1] and s2[j-1]==s3[i+j-1])or  (dp[i-1][j] and s1[i-1]==s3[i+j-1])
                    
             return dp[-1][-1]
#         cach={}            
#         def dfs(i,h,k):
#             if h>len(s1) or k>len(s2):return False
#             if i==len(s3):
#                 if h==len(s1) and k==len(s2):return True
#                 return False
#             if (i,h,k) in cach:return cach[(i,h,k)]
#             if h<len(s1) and k<len(s2) and s3[i]==s1[h] ==s2[k]:
#                 cach[(i,h,k)]= dfs(i+1,h+1,k) or dfs(i+1,h,k+1)
                
#             elif h<len(s1) and s3[i]==s1[h]: cach[(i,h,k)]= dfs(i+1,h+1,k)
#             elif k<len(s2) and s3[i]==s2[k]:cach[(i,h,k)]= dfs(i+1,h,k+1)
#             else: cach[(i,h,k)]=False
                
#             return cach[(i,h,k)]
                    
#         return dfs(0,0,0) 
                    
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