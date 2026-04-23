class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        mySet = set()
        for x in nums:
            mySet.add(x)       
         
        myList = []
        for x in mySet:
            myList.append(x)
        
        myList.sort()
        j = 0
        counter = 0
        maxVal = 0
        print(myList)
        while j < len(myList):
            if j + 1  == len(myList):
                return maxVal + 1

            if 1 == abs(myList[j + 1] - myList[j]):
                counter = 1 + counter
            else:
                maxVal = max(maxVal, counter)
                counter = 0
            maxVal = max(maxVal, counter)
            j = 1 + j
                     


        


