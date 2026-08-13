class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []

        temp = []

        def helper(i):
            if i == len(nums):
                final.append(temp[:])
                return
            
            
            temp.append(nums[i])

            helper(i + 1)

            temp.pop()
            helper(i + 1)
             


        helper(0)
        return final
            

