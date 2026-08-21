class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myDict = {}



        for i in nums:
            myDict[i] = myDict.get(i, 0) + 1

        final = []
        
        for i in range(k):
            temp = max(myDict, key=myDict.get)
            final.append(temp)
            myDict.pop(temp)
        return final

