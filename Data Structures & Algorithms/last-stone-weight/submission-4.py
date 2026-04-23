class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            max1 = stones[-1]
            max2 = stones[-2]
           

            if max1 == max2:
                stones.remove(max2)
                stones.remove(max1)
            elif max1 > max2:
                temp = max1 - max2
                stones[stones.index(max1)] = temp
                stones.remove(max2)
                stones.sort()
            else:
                temp = max2 - max1
                stones[stones.index(max2)] = temp
                stones.remove(max1)
                stones.sort()
        if not stones:
            return 0
        else:    
            return stones[0]
