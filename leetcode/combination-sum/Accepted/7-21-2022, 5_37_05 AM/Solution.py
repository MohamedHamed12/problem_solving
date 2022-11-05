// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
                res = []
    
                def dfs(i, cur, total):
                    if total == target:
                        res.append(cur.copy())
                        return
                    if i >= len(candidates) or total > target:
                        return

                    cur.append(candidates[i])
                    dfs(i, cur, total + candidates[i])
                    cur.pop()
                    dfs(i+1, cur, total)


                dfs(0, [], 0)     
                return res


# n=len(l)
#         tot=[]
#         c=[combinations(l,i) for i in range(0,n+1)]
#         for i in c:
#             r=filter(lambda x: sum(x)==5, i)
#             for j in r:
#               tot.append(list(j))

#         return tot
        # for i in tot:
        #     for j in i:
        #       print(j)
    # n=len(candidates)
        # c=[combinations(candidates,i) for i in range(0,n)]
        # tot=[]
        # for i in c:
        #     for j in i:
        #      if sum(j)==target:
        #         tot.append(j)
        # return tot