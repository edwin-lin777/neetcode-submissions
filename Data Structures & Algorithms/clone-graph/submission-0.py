"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        temp = {}

        def helper(node):
            if node in temp:
                return temp[node]
            if node is None:
                return None
            temp[node] = Node(node.val)
            for n in node.neighbors:
                temp[node].neighbors.append(helper(n))
            
            return temp[node]
        
        return helper(node)

