# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.count = 0
        def getCount(curr):
            if curr == None:
                return 0
            return 1 + max(getCount(curr.left), getCount(curr.right))
        
        def helper2(curr):
            if curr == None:
                return True
            
            if abs(getCount(curr.left) - getCount(curr.right) )> 1:
                return False
            
            
            return helper2(curr.left) and helper2(curr.right)

        
        return helper2(root)

            