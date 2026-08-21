class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowSet = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowSet:
                    return False
                else:
                    rowSet.add(board[i][j])
        
        for i in range(9):
            colSet = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in colSet:
                    return False
                else:
                    colSet.add(board[j][i])
        

        box = defaultdict(set)
        for r in range(9):

            for j in range(9):
                if board[r][j] == ".":
                    continue                    
                val = board[r][j]
                if val in box[(r // 3, j // 3)]:
                    return False
                else:
                    box[(r // 3, j // 3)].add(val)
        
        return True
                


