class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        myDict = {}
        for i in range(n):
            myDict[i] = []
        for left, right in edges:
            myDict[left].append(right)
            myDict[right].append(left)

        count = 0
        mySet = set()
        def helper(i):        
            if i in mySet:
                return
        
            mySet.add(i)
            for j in myDict[i]:
                helper(j)
            return

        for temp in range(n):
            if temp in mySet:
                continue
            helper(temp)
            count += 1
        return count


        

