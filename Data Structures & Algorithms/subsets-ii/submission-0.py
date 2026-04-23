class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        final = []
        res = []

        n = len(nums)
        def helper(i):
            if i == n:
                final.append(res[:])
                return
            
            res.append(nums[i])
            helper(i + 1)
            res.pop()

            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1)

        helper(0)
        return final



