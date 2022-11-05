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
class Solution: # Python
    def minCost(self, n: int, cuts: List[int]) -> int:
        @functools.lru_cache(None)
        def fn(lo, hi):
            cc = [c for c in cuts if lo < c < hi]  # collect cuts within this region
            if not cc:
                return 0
            ans = float('inf')
            for mid in cc: # choose a cut in that is in the region to be mid
                ans = min(ans, fn(lo, mid) + fn(mid, hi))
            return ans + hi - lo # ans + currentCut
        return fn(0, n)