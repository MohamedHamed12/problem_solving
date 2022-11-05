// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, dig: str) -> List[str]:
        if not dig:return
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        l=[]
        def dfs(ind,tem):
            if ind ==len(dig):
                l.append("".join(tem) )
                return
            for i in d[dig[ind]]:
                dfs(ind+1,tem+[i])
        dfs(0,[])
        return l