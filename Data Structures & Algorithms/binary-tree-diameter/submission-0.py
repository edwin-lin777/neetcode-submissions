# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def dsf(curr):
            if curr == None:
                return 0
            
            left = dsf(curr.left)
            right = dsf(curr.right)
            self.count = max(self.count, left + right)
            return 1 + max(left,right)
        
        dsf(root)
        return self.count
