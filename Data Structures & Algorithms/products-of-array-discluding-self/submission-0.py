class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = [];
        for i in range(len(nums)):
            temp = 1;
            for j in range(len(nums)):
                if i != j:
                    temp = temp * nums[j]
            final.append(temp)
        return final
