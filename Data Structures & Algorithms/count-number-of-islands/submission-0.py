class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0

        def helper(r, c):
    
            if (r < 0 or c < 0 or
                    r >= row or c >= col or 
                    0 == grid[r][c]):
        
                    return

            if grid[r][c] == "1":
                grid[r][c] = 0
                helper(r, c - 1) 
                helper(r, c + 1) 
                helper(r - 1, c) 
                helper(r + 1, c)
            
        for r in range(row):          
                for c in range(col):
                    if grid[r][c] == "1":
                        count += 1
                        helper(r, c)
            
        return count

        
    
        
        
        
            
