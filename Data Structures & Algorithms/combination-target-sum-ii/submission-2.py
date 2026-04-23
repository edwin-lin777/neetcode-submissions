class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def summer(array):
            mysum = 0
            for i in range(len(array)):
                mysum += array[i]
            return mysum


        n = len(candidates)
        final = []
        sol = []

        def helper(i):
            temp = summer(sol)
            if temp > target:
                return

            if temp == target:
                final.append(sol[:])
                return
            if i == n:
                return

            
            
            
            sol.append(candidates[i]) 
            helper(i + 1)
            sol.pop()     
            
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            helper(i + 1)

        helper(0)
        

        return final