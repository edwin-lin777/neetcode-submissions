class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
         
        result = right
         
        
        while left <= right:
            hours = 0
            mid = (left + right) // 2
            for i in range(len(piles)):
                hours += (piles[i] + mid - 1) // mid
            
            if hours <= h:
                right = mid - 1
                result = min(result, mid)
            if hours > h:
                left = mid + 1
        
        return result
         
