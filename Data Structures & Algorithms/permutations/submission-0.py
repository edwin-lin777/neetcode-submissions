class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []
        sol = []
        
        def helper(lst):
            if len(lst) == 0:
                return [[]]
            
            permutations = helper(lst[1:])

            result = []
            for p in permutations:
                for i in range(len(p) + 1):
                    temp = p.copy()
                    temp.insert(i, lst[0])
                    result.append(temp)
                    
            return result


        return helper(nums)


             

