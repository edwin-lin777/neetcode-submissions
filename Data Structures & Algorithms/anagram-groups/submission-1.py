class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        
        for w in strs:
            temp = ''.join(sorted(w))   
            if temp in myDict:
                myDict[temp].append(w)
            else:
                myDict[temp] = [w]


        
        final = []
        for temp in myDict:
            final.append(myDict.get(temp))

        return final