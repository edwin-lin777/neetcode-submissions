class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        myDict = {}
        for i in range(n):
            myDict[i] = []

        for node, direction in edges:
            myDict[node].append(direction)
            myDict[direction].append(node)
        seen = set()

        def helper(n, prev):
            if n in seen:
                return False
            seen.add(n)
            for temp in myDict[n]:
                if temp == prev:
                    continue
                if not helper(temp, n):
                    return False
            return True
        
        return helper(0, -1) and len(seen) == n
            
            
      

