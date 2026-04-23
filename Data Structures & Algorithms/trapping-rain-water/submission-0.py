class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0;
        end = len(height) - 1
        maxL = height[start]
        maxR = height[end]
        final = 0
        while start < end:
            if maxL < maxR:
                start += 1
                maxL = max(maxL, height[start])
                final += (maxL - height[start])
            else: 
                end -= 1
                maxR = max(maxR, height[end])
                final += (maxR - height[end])
        return final



        