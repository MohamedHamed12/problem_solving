// https://leetcode.com/problems/n-queens

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        dneg=set()
        dpos=set()
        res=[]
        board=[['.']*n for i in range(n)]
        def bactrack(r):
            if r==n:
                res.append(["".join(i) for i in board])
            for c in range(n):
                if c in col or r+c in dpos or r-c in dneg :continue
                col.add(c) ;dpos.add(r+c );dneg.add(r-c)
                board[r][c]='Q'
                bactrack(r+1)
                col.remove(c) ;dpos.remove(r+c );dneg.remove(r-c)
                board[r][c]='.'     
        
        bactrack(0)
        return res