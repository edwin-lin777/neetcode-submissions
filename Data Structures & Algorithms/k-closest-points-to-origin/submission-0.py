class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
       
        heap = []

        for x, y in points:
            dist = (x ** 2 + y ** 2) ** 0.5
            heapq.heappush(heap, [dist, x, y])
        
        result = []
        for i in range(k):
            
            temp = heapq.heappop(heap)
            result.append(temp[1:])
        return result
