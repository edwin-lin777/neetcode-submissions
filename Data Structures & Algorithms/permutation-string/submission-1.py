class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        myDictionary = {}
        for i in range(len(s1)):
            myDictionary[s1[i]] = myDictionary.get(s1[i], 0) + 1
        length = len(s1)
        myDict2 = {}
        for i in range(len(s2) - length + 1):
            for j in range(length):
                myDict2[s2[j + i]] = myDict2.get(s2[j + i], 0) + 1
            
            if myDict2 == myDictionary:
                return True
            myDict2.clear()
        
        return False


