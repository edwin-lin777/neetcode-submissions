class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mySet = set()

        for i in range(len(nums)):
            if nums[i] not in mySet:
                mySet.add(nums[i])
            else:
                return nums[i]

    

        