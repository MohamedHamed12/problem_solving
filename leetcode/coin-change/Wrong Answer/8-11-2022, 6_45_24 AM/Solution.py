// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*((amount)+1)
        dp[0]=0
        
        for i in range(1,len(dp)):
            for c in coins:
                if i-c>=0:
                  dp[i]=min(dp[i],1+dp[i-c])
        return dp[-1] if dp[-1]!=amount else -1
#         reachableAmount = 1 << amount
#         count = 0

#         while reachableAmount & 1 == 0:
            
#             reachableAmount_backup = reachableAmount
            
#             for coin in coins:
#                 reachableAmount |= reachableAmount_backup >> coin
                
#             if reachableAmount == reachableAmount_backup:
#                 return -1
            
#             count += 1
        
#         return count
    
# def main():
#     obj = Solution()
#     ans = obj.coinChange([1,2,5], 11)
    
# main()

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         def _coinChange(coins, amount, memo):
#             if amount in memo:
#                 return memo[amount]
#             if amount == 0:
#                 return 0
#             if amount < 0:
#                 return float('inf')
#             min_coins = float('inf')
#             for coin in coins:
#                 num_coins = 1 + _coinChange(coins, amount - coin, memo)
#                 min_coins = min(min_coins, num_coins)
#             memo[amount]= min_coins
#             return min_coins
        
#         ans = _coinChange(coins, amount, {})
#         if ans == float('inf'):
#             return -1
#         else:
#             return ans
# class Solution:
#      def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [amount + 1] * (amount + 1)
#         dp[0] = 0
        
#         for a in range (1, amount + 1):
#             for c in coins:
#                 if (a - c) >= 0:
#                     dp[a] = min(dp[a], 1 + dp[a-c])
#         return dp[amount] if dp[amount] != amount + 1 else -1
#     def coinChange(self, l,n) :
#           # l=sorted(l)
#           if n==0:return 0
#           tot=[float('inf')]*(n+1) 
#           for i in l:
#             for j in range(n+1):

#                 if j<i:continue
#                 elif i==j:tot[j]=1
#                 else:tot[j]=min(tot[j],1+tot[j-i])
#           return tot[-1] if tot[-1]!=float('inf') else -1
#         # l=sorted(l)
#         # tot=0
#         # for i in l[::-1]:
#         #     tot+=c//i
#         #     c=c%i
#         #     if c==0:return tot
#         # if c==0:return tot
#         # else:return -1
