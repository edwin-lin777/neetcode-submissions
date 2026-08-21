class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        count = len(t)
        lengthT = len(t) - 1
        i = 0
        j = 0
        lengthS = len(s) - 1
        while i <= lengthT and j <= lengthS:
            if s[j] == t[i]:
                i += 1
                j += 1
                count -= 1
            else:
                j += 1
                
        return count