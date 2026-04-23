# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def helper(preorder, inorder):
            if not preorder or not inorder:
                return
            
            root = inorder.index(preorder[0])
            tree = TreeNode(preorder[0])
            
            tree.left = helper(preorder[1: root + 1], inorder[0: root] )
            tree.right = helper(preorder[root + 1:], inorder[root + 1:])
            return tree
        

        return helper(preorder, inorder)