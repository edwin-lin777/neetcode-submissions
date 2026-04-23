class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        list(set(candidates))

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

            helper(i + 1)

            sol.append(candidates[i]) 
            helper(i + 1)
            sol.pop()      
        helper(0)
        

        a = []
        for i in range(len(final)):
            temp = sorted(final[i])
            if temp not in a:
                a.append(temp)

        return a