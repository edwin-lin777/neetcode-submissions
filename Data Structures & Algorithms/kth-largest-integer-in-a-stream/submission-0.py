class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.largest = k
        self.lst = nums

    def add(self, val: int) -> int:
        self.lst.append(val)
        self.lst.sort()
        temp = self.largest
        return self.lst[-temp]
