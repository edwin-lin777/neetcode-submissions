class Solution:
    def maxArea(self, heights: List[int]) -> int:
        final = 0

        for i in range(len(heights)):

            CurrMax = 0
            for j in range(i + 1, len(heights)):
                temp = min(heights[i], heights[j])
                temp *= j - i
                CurrMax = max(temp, CurrMax)

            final = max(final, CurrMax)
        return final 