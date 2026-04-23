class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
            myDict = {}
            for i in range(n):
                myDict[i + 1] = []
            for node, target, time in times:
                myDict[node].append((target,time))
            
            dist = {}
            minHeap = [(0, k)]

            while minHeap:
                cost, node = heapq.heappop(minHeap)
                if node in dist:
                    continue
                dist[node] = cost

                for neighbor, time in myDict[node]:
                    if neighbor not in dist:
                        heapq.heappush(minHeap, (cost + time, neighbor))
            if len(dist) < n:
                return -1
        
            return max(dist.values())
            
                
            


            







                
