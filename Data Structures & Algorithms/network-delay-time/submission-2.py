class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        myDict = {}

        for i in range(n):
            myDict[i+ 1] = []

        for source, target, time in times:
            myDict[source].append((time, target))
        
        visited = set()
        myHeap = [(0, k)]

        time = 0

        while myHeap:
            t, node = heapq.heappop(myHeap)
            if node in visited:
                continue
            visited.add(node)
            time = max(t, time)
            for timeNode, target in myDict[node]:
                if target not in visited:
                    heapq.heappush(myHeap, (timeNode + t, target))

        if len(visited) != n:
            return -1
        return time