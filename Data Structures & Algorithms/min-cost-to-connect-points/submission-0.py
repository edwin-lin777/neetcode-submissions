class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        myDict = {}
        for i in range(len(points)):
            myDict[i] = []

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                myDict[i].append([dist, j])
                myDict[j].append([dist, i])

        res = 0
        visited = set()
        minH = [[0,0]]
        while len(visited) < len(points):
            cost, node = heapq.heappop(minH)
            if node in visited:
                continue
            visited.add(node)
            res += cost
            for neiCost, nei in myDict[node]:
                if nei not in visited:
                    heapq.heappush(minH, [neiCost, nei])

        return res
