// https://leetcode.com/problems/minimum-cost-to-cut-a-stick

class Solution:
    def minCost(self, lenght: int, lst: List[int]) -> int:
         
            n = len(lst)
            lst = sorted(lst)
            lst.insert(0, 0)
            lst.append(lenght)
            cache = {}
            @lru_cache(maxsize=8192)
            def dfs(l, r):
                if (l, r) in cache:
                    return cache[(l, r)]
                if r-l == 1:
                    return 0
                ans = float('inf')
                for i in range(len(lst)):
                    if i > l and i < r:
                        ans = min(ans, dfs(l, i)+dfs(i, r)+lst[r]-lst[l])
                cache[(l, r)] = ans
                return ans
            return dfs(0, n+1)