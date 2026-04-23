class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        start = 0
        end = length - 1
        for i in range(length):
            if numbers[start] + numbers[end] == target:
               
                return [start + 1, end + 1]
            if numbers[start] + numbers[end] < target:
                start = start + 1
            else: 
                end = end - 1