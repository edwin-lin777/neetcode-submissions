class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])


        def helper(r, c, distance):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == -1:
                return

            if grid[r][c] == 0 and distance != 0:
                return
            if grid[r][c] != 0 and grid[r][c] < distance:
                return
            
            if grid[r][c] != 0:
                grid[r][c] = distance
            helper(r + 1, c, distance + 1)
            helper(r - 1, c, distance + 1)
            helper(r, c - 1, distance + 1)
            helper(r, c + 1, distance + 1)

        
        
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    helper(r, c, 0)
        

