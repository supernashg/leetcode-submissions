class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        cols = set()
        pos_diags = set()
        neg_diags = set()
        nqueens = []

        def backtrack(r):
            if r == n:
                nqueens.append([''.join(row) for row in board])
                return


            for c in range(n):
                if c not in cols and c + r not in pos_diags and c - r not in neg_diags:
                    cols.add(c)
                    pos_diags.add(c + r)
                    neg_diags.add(c - r)
                    board[r][c] = 'Q'
                    backtrack(r + 1)
                    cols.remove(c)
                    pos_diags.remove(c + r)
                    neg_diags.remove(c - r)
                    board[r][c] = '.'
        backtrack(0)
        return nqueens

