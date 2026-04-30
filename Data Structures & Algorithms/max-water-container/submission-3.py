class Solution:
    def maxArea(self, heights: List[int]) -> int:
        final = 0
        left = 0
        right = len(heights) - 1

        while left <= right:
            temp = min(heights[left], heights[right])

            temp *= (right - left)

            final = max(final, temp)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1


        return final