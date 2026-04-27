class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        for i in range(len(nums)):
            temp = nums[i]
            currMax = max(currMax, temp)
            for j in range(i + 1, len(nums)):
                
                temp = temp * nums[j]

                currMax = max(currMax, temp)

        currMax = max(currMax, nums[len(nums) - 1])
        return currMax