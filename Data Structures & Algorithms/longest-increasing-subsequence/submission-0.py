class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = (len(nums)) * [1]
        LIS[len(nums) - 1] = 1
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)

        return max(LIS)