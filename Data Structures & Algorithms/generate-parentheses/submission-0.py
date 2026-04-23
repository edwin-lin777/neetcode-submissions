class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        myOpen = 0
        myClose = 0
        final = []
        sol = []
        

        def helper(myOpen, myClose):
            if myOpen == 0 and myClose == 0:
                final.append("".join(sol))
            
            if myOpen > 0:
                sol.append("(")
                helper(myOpen - 1, myClose)
                sol.pop()
            if myOpen < myClose:
                sol.append(")")
                helper(myOpen, myClose - 1)
                sol.pop()
        
        helper(n, n)
        return final


