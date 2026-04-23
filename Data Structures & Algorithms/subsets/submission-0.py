class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        sol = []
        n = len(nums)
        def helper(i):
            if i == n:
                final.append(sol[:])
                return
            helper(i + 1)

            sol.append(nums[i])
            helper(i + 1)
            sol.pop()

        helper(0)
        return final