class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mySet = set()
 
        right = len(heights) - 1 

        while right > 0:
            for i in range(right):
                mySet.add(min(heights[i], heights[right]) * (right - i))
            right = right - 1
        return max(mySet)


