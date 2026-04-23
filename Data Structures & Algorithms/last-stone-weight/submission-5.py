class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)
        while len(stones) > 1:
            max1 = heapq.heappop(stones)
            max2 = heapq.heappop(stones)
         
            if max1 < max2:
                heapq.heappush(stones, max1 - max2)
            if max1 > max2:
                heapq.heappush(stones, max2 - max1)
                

        if not stones:
            return 0
        else:
            return -stones[0]


