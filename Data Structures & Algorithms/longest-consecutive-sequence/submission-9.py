class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        count = 0
        maxVal = 0
        i = 0
        if not nums:
            return 0
        for x in mySet:
            count = 0
            while x + 1 in mySet:
                count = 1 + count
                x += 1
            maxVal = max(maxVal, count)

        return maxVal + 1