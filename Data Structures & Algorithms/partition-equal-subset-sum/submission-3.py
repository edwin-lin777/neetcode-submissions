class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        temp = sum(nums)

        if temp % 2 != 0:
            return False
        target = temp // 2

        mySet = set()
        mySet.add(0)

        for i in range(len(nums) - 1, -1, -1):
            mySet = mySet | {x + nums[i] for x in mySet} 

        return target in mySet