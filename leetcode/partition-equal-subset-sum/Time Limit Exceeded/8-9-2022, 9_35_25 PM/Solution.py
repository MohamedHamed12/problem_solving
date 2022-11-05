// https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, l: List[int]) -> bool:
        s=sum(l)
        if (s//2)*2!=s:return False
        dp=[False]*(1+s//2)
        def  dfs(ind ,tem):
             if ind >=len(dp):return 
             for i in range(len(tem)):
                if ind+tem[i] <len(dp) :
                    dp[ind+tem[i]]=True
                    dfs(ind+tem[i],tem[:i]+tem[i+1:])
            
        dfs(0,l)
        return dp[-1]