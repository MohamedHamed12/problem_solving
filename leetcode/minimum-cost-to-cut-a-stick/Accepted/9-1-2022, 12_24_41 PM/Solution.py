// https://leetcode.com/problems/minimum-cost-to-cut-a-stick

# class Solution:
#     def minCost(self, lenght: int, lst: List[int]) -> int:
         
#             n = len(lst)
#             lst = sorted(lst)
#             lst.insert(0, 0)
#             lst.append(lenght)
#             cache = {}
#             @lru_cache(maxsize=8192)
#             def dfs(l, r):
#                 if (l, r) in cache:
#                     return cache[(l, r)]
#                 if r-l == 1:
#                     return 0
#                 ans = float('inf')
#                 for i in range(len(lst)):
#                     if i > l and i < r:
#                         ans = min(ans, dfs(l, i)+dfs(i, r)+lst[r]-lst[l])
#                 cache[(l, r)] = ans
#                 return ans
#             return dfs(0, n+1)
# class Solution:
#     def minCost(self, n: int, cuts: List[int]) -> int:
#         cuts.extend([0,n])
#         cuts.sort()
#         l = len(cuts)
#         dp = [[float('inf')]*l for _ in range(l)]
#         for i in range(l):
#             for j in range(2):
#                 if i+j < l:
#                     dp[i][i+j] = 0
#         for k in range(2,l):
#             for i in range(l-k):
#                 for j in range(i+1,i+k):
#                     dp[i][i+k] = min(dp[i][i+k],cuts[i+k]-cuts[i]+dp[i][j]+dp[j][i+k])
#         return dp[0][l-1]
# class Solution: # Python
    # def minCost(self, n: int, cuts: List[int]) -> int:
    #     @functools.lru_cache(None)
    #     def fn(lo, hi):
    #         cc = [c for c in cuts if lo < c < hi]  # collect cuts within this region
    #         if not cc:
    #             return 0
    #         ans = float('inf')
    #         for mid in cc: # choose a cut in that is in the region to be mid
    #             ans = min(ans, fn(lo, mid) + fn(mid, hi))
    #         return ans + hi - lo # ans + currentCut
    #     return fn(0, n)
     # def minCost(self, N: int, cuts: List[int]) -> int:
     #    c=len(cuts)
     #    cuts.append(0)
     #    cuts.append(N)
     #    cuts.sort()
     #    dp=[[0 for i in range(c+2)]for j in range(c+2)]  
     #    for i in range(c,0,-1):
     #        for j in range(1,c+1):
     #            if i>j:
     #                continue
     #            mini=float("inf")
     #            for ind in range(i,j+1):
     #                cost=cuts[j+1]-cuts[i-1] +dp[i][ind-1] + dp[ind+1][j]
     #                mini=min(mini,cost)
     #            dp[i][j]=mini
     #    return dp[1][c]
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        dp = [[0] * len(cuts) for _ in range(len(cuts))]
        for i in range(len(cuts) - 1, -1, -1):
            for j in range(i + 1, len(cuts)):
                if j - i == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i][k] + dp[k][j] for k in range(i + 1, j)) + cuts[j] - cuts[i]
        return dp[0][-1]
