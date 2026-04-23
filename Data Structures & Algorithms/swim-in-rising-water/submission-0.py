class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        mySet = set()
        myHeap = [(grid[0][0], 0, 0)]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        mySet.add((0,0))

        while myHeap:
            time, r, c = heapq.heappop(myHeap)
            
            if r == row - 1 and c == col - 1:
                return time
            for dr, dc in directions:
                neiR, neiC = dr + r, dc + c
                if neiR < 0 or neiC < 0 or neiR >= row or neiC >= col or (neiR, neiC) in mySet:
                    continue
                mySet.add((neiR, neiC))
                heapq.heappush(myHeap, (max(time, grid[neiR][neiC]), neiR, neiC))

