class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        maxCount = 0

        def helper(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == 0:

                return 0

            if grid[r][c] == 1:
                grid[r][c] = 0
                return helper(r + 1, c) + helper( r - 1, c) + helper(r, c + 1) + helper(r, c - 1) + 1
            
        for r in range(row):
            for c in range(col):
                temp = helper(r, c)
                maxCount = max(maxCount, temp)
        return maxCount
            

                
                
