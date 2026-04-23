class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
        
        for i in s:
            countS[i] = 1 + countS.get(i, 0)

        for i in t:
            countT[i] = 1 + countT.get(i, 0)
         
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

        