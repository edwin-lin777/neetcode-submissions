class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for x in range(9):
            mySet = set()
            for y in board[x]:
                if y == ".":
                    continue
                if y in mySet:
                    return False
                mySet.add(y)

        for x in range(9):
            mySet = set()
            for y in range(9):
                if board[y][x] == ".":
                    continue
                if board[y][x] in mySet:
                    return False
                mySet.add(board[y][x])


        for row in range(3):
            for col in range(3):
                mySet = set()
                for j in range(col * 3, (col + 1)* 3):
                    for i in range(row * 3, (row + 1) * 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in mySet:
                            return False
                        mySet.add(board[i][j])

        return True
            