class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = int (len(nums) / 2)
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        while len(nums) > 1:
             
            first = nums[: int(len(nums) / 2)]
            second = nums[int(len(nums) / 2) :]

            if second[0] == target:
                return index

            if first[-1] == target:
                return index - 1

            if target > second[0]:
                nums = second
                index += int(len(second) / 2)
            else:
                nums = first
                index -= 1 + int((len(first) / 2) ) 
        return -1

