# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def __init__(self):
        self.final = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.helper(root, 0)

        return self.final
        

    def helper(self, root, count):
        if root == None:
            self.final = max(self.final, count)
            return
        
        self.helper(root.left, count = count + 1)
        self.helper(root.right, count = count + 1)
        
