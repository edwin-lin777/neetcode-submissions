# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       
        def helper(node, hi, lo):
            if node is None:
                return True
            
            if  lo >= node.val or node.val >= hi:
                return False
            return helper(node.left, node.val, lo) and helper(node.right, hi, node.val)

        return helper(root, float('inf'), float('-inf'))

