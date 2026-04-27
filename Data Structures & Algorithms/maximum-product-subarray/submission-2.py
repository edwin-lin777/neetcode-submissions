class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        myMax = max(nums)
        currMax, currMin = 1,1

        for i in range(len(nums)):
            if nums[i] == 0:
                currMin = 1
                currMax = 1
            else:
                temp = currMax
                currMax = max(nums[i] * currMin, nums[i] * temp, nums[i])
                currMin = min(nums[i] * currMin, nums[i] * temp, nums[i])
                if myMax < currMax:
                    myMax = currMax
        return myMax