// https://leetcode.com/problems/coin-change

class Solution:
     def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for a in range (1, amount + 1):
            for c in coins:
                if (a - c) >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return dp[amount] if dp[amount] != amount + 1 else -1
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
