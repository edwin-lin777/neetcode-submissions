class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stack = {}

        for x in range(len(nums)):
            difference = target - nums[x];
            if difference in stack:
                return [stack[difference], x]
            stack[nums[x]] = x
    

