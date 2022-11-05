// https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
            n = len(board)
            r = defaultdict(set)
            c = defaultdict(set)
            b = defaultdict(set)
            for i in range(n):
                for j in range(n):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in r[i] or board[i][j] in c[j] or board[i][j] in b[(i//3, j//3)]:
                        return False

                    r[i].add(board[i][j])
                    c[j].add(board[i][j])
                    b[(i//3, j//3)].add(board[i][j])
            return True
        
        # for i in range(9):
        #     row = ""
        #     col = ""
        #     box = ""
        #     for j in range(9):
        #         #check row
        #         if board[i][j] != ".":
        #             if board[i][j] not in row:
        #                 row += board[i][j]
        #             else:
        #                 print(row)
        #                 return False
        #         #check col
        #         if board[j][i] != ".":
        #             if board[j][i] not in col:
        #                 col += board[j][i]
        #             else:
        #                 return False
        #         #check box
        #         bi = (i//3)*3 + j//3
        #         bj = (i%3)*3 + j%3
        #         if board[bi][bj] != ".":
        #             if board[bi][bj] not in box:
        #                 box += board[bi][bj]
        #             else:
        #                 return False
        # return True