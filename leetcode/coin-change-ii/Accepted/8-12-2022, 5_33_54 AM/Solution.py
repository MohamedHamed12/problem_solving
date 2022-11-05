// https://leetcode.com/problems/coin-change-ii

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[0]*(amount+1) for i in range(len(coins)+1)]
        coins=sorted(coins)
        for i in range(len(coins)+1 ):
            for j in range(amount+1):
                if j==0 :dp[i][j]=1
                elif i==0:dp[i][j]=0
                elif j<coins[i-1]:dp[i][j]=dp[i-1][j]
                else:dp[i][j]=dp[i-1][j]+dp[i][j-coins[i-1]]
        
        
        return dp[-1][-1]
        
        
        
        
        
        # cach={}
        # def dfs(i,tmpsum):
        #     if i>=len(coins):return 0
        #     if tmpsum>amount:return 0
        #     if tmpsum==amount:return 1
        #     if (i,tmpsum) in cach:return cach[(i,tmpsum)]
        #     cach[(i,tmpsum)]=dfs(i,tmpsum+coins[i])+dfs(i+1,tmpsum)
        #     return cach[(i,tmpsum)]
        # return dfs(0,0)