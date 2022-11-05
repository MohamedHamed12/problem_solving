// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def dfs(i,buy):
            if i>=len(prices):return 0
            if (i,buy) in dp:return dp[(i,buy)]
            
            cool=dfs(i+1,buy)
            if buy:
                bbuy=dfs(i+1,not buy)-prices[i]
                dp[(i,buy)]=max(cool,bbuy)
            else:
                sell=dfs(i+2,not buy)+prices[i]
                dp[(i,buy)]=max(sell,cool)
            return dp[(i,buy)]
        
        return dfs(0,True)