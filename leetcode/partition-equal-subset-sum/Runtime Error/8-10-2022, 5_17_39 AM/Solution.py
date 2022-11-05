// https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, l: List[int]) -> bool:
        st=set()
        s=sum(l)
        if (s//2)*2!=s:return False
        t=s//2
        st=set()
        for i in l:st.add(i)
        for i in l:
            for j in st:st.add(i*j)
            if t in st:return True
        return False
        
        
        # dp=[False]*(1+s//2)
#         def  dfs(ind ,tem):
#              if ind >=len(dp):return 
#              for i in range(len(tem)):
#                 if ind+tem[i] <len(dp) :
#                     dp[ind+tem[i]]=True
#                     dfs(ind+tem[i],tem[:i]+tem[i+1:])
            
#         dfs(0,l)
#         return dp[-1]