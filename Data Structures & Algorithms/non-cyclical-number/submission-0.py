class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        def helper(n):
            temp = n
            mySum = 0
            while temp != 0:
                mySum += (temp % 10) * (temp % 10)
                temp = temp // 10

            if mySum == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            

            return helper(mySum)            



        return helper(n)
