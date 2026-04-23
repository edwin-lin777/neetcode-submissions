class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        final = []
        myDict = {2: ["a", "b","c"],
                    3: ["d", "e", "f"],
                    4: ["g", "h", "i"],
                    5: ["j", "k","l"],
                    6: ["m", "n", "o"],
                    7: ["p", "q", "r", "s"],
                    8: ["t","u","v"],
                    9: ["w", "x", "y", "z"]
                    }
        def helper(i):
            if i == len(digits):
                final.append("".join(res[:]))
                return
            temp = int(digits[i])
            for j in range(len(myDict[temp])):
                res.append(myDict[temp][j])
                helper(i + 1)
                res.pop()

        helper(0)
        if final[0] == "":
            return []
        return final

            

            