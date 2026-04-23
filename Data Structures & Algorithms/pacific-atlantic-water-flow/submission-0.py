class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])

        pacific = set()
        atlantic = set()

        def helper(r, c, before, pacificorNot):
            if r < 0 or c < 0 or r >= row or c >= col:
                return
            if heights[r][c] < before:
                return

            if pacificorNot and (r,c) in pacific:
                return
            if not pacificorNot and (r,c) in atlantic:
                return
            if pacificorNot:
                pacific.add((r,c))
            if not pacificorNot:
                atlantic.add((r,c))
            
            helper(r + 1, c, heights[r][c], pacificorNot)
            helper(r - 1, c, heights[r][c], pacificorNot)
            helper(r, c + 1, heights[r][c], pacificorNot)
            helper(r, c - 1, heights[r][c], pacificorNot)

        
        for r in range(row):
            helper(r, 0, heights[r][0], True)
            helper(r, col - 1, heights[r][col - 1], False)
        for c in range(col):
            helper(0, c, heights[0][c], True)
            helper(row - 1, c, heights[row - 1][c], False)

        set3 = pacific & atlantic
        
        return [list(coord) for coord in set3]



