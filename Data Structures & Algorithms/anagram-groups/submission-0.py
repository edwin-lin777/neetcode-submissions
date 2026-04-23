class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = {}

        for x in strs:
            sortedWord = "".join(sorted(x))
            if sortedWord not in final:
                final[sortedWord] = [x];
            else:
                final[sortedWord].append(x)


        finalList = []
        for x in final:
            finalList.append(final[x])

        return finalList;
            

            
