// https://leetcode.com/problems/coin-change-ii

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp=[[float('')]]
        cach={}
        def dfs(i,tmpsum):
            if i>=len(coins):return 0
            if tmpsum>amount:return 0
            if tmpsum==amount:return 1
            if (i,tmpsum) in cach:return cach[(i,tmpsum)]
            cach[(i,tmpsum)]=dfs(i,tmpsum+coins[i])+dfs(i+1,tmpsum)
            return cach[(i,tmpsum)]
        return dfs(0,0)