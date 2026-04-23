class Solution:
    def solve(self, board: List[List[str]]) -> None:
        surrounded = set()

        row = len(board)
        col = len(board[0])


        def helper(r, c):
            if r < 0 or c < 0 or c >= col or r >= row:
                return
            
            if board[r][c] == 'X' or (r, c) in surrounded:
                return
            surrounded.add((r, c))
            
            helper(r + 1, c)
            helper(r - 1, c)
            helper(r, c + 1)
            helper(r, c - 1)
        
        for r in range(row):
            if board[r][0] == 'O':
                helper(r, 0)
            if board[r][col - 1] == 'O':
                helper(r, col - 1)

        for c in range(col):
            if board[0][c] == 'O':
                helper(0, c)
            if board[row - 1][c] == 'O':
                helper(row - 1, c)
        for r in range(row):
            for c in range(col):
                if (r,c) not in surrounded:
                    if board[r][c] == 'O':
                        board[r][c] = 'X'

        
            
