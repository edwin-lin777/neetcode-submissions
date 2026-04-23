class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mySet = set()
        for i in range(len(prices)):

           for j in range(len(prices)):
                if i >= j:
                    continue
                mySet.add(prices[j] - prices[i])
        if len(prices) == 1:
            return 0
        if max(mySet) <= 0:
            return 0
        return max(mySet) 
