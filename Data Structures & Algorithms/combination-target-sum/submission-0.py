class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        final = []

        n = len(nums)

        def summer(array: List[int]):
            temp = 0;
            for i in range(len(array)):
                temp += array[i]
            return temp

        def helper(i):
            tempSum = summer(result[:])
            if tempSum > target:
                return

            if tempSum == target:
                final.append(result[:])
                return
            if i == n:
                return
            
            
            result.append(nums[i])
            helper(i)
            result.pop()

            helper(i + 1)
            
        helper(0)
        return final
