class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        row = len(grid)
        col = len(grid[0])
        fresh = 0
        time = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while fresh > 0 and q:
            for i in range(len(q)):
                dr, dc = q.popleft()
                for r, c in directions:
                    Trow = dr + r
                    Tcol = dc + c
                    if Trow < 0 or Tcol < 0 or Trow >= len(grid) or Tcol >= len(grid[0]) or grid[Trow][Tcol] != 1:
                        continue
                    grid[Trow][Tcol] = 2
                    fresh -= 1
                    q.append([Trow, Tcol])
            time += 1

        return time if fresh == 0 else -1




