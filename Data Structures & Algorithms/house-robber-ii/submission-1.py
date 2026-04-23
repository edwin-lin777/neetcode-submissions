class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        
        tempar = nums[:-1]
        for n in tempar:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        temp1 = 0
        temp2 = 0
        myVal = nums[0]
        nums = nums[1:]
        

        for n in nums:
            tempV = max(n + temp1, temp2)
            temp1 = temp2
            temp2 = tempV
        
        return max(temp2, rob2, myVal)
