// https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        mask, target = 0, total // 2
        
        for n in nums:
            mask |= (mask << n)
            mask |= (1 << (n-1))
        return mask & (1 << (target - 1))
#         st=set()
#         s=sum(l)
#         if (s//2)*2!=s:return False
#         t=s//2
#         st=set([0])
#         # for i in l:st.add(i)
#         for i in l:
#             tem=st.copy()
#             for j in tem:
#                 st.add(i+j)
#                 if i+j ==t:return True
                
            
#         return False
        # s=sum(l)
        # if (s//2)*2!=s:return False
        # t=s//2
        # for mask in range(1<<len(l)):
        #     tem=0
        #     for j in range(mask.bit_length()+1):
        #         if mask &(1<<j):tem+=l[j]
        #     if tem==t:return True
        # return False
#         st=set()
#         s=sum(l)
#         if (s//2)*2!=s:return False
#         t=s//2
#         st=set([0])
#         # for i in l:st.add(i)
#         for i in l:
#             tem=st.copy()
#             for j in tem:
#                 st.add(i+j)
#                 if i+j ==t:return True
                
            
#         return False
        
        
        
        
        
        
        
        
        
        
        
        # dp=[False]*(1+s//2)
#         def  dfs(ind ,tem):
#              if ind >=len(dp):return 
#              for i in range(len(tem)):
#                 if ind+tem[i] <len(dp) :
#                     dp[ind+tem[i]]=True
#                     dfs(ind+tem[i],tem[:i]+tem[i+1:])
            
#         dfs(0,l)
#         return dp[-1]