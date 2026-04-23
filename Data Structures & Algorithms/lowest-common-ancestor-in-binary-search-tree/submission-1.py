# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def helper(curr, p, q):
            if p.val < curr.val and q.val > curr.val:
                return curr
            if p.val > curr.val and q.val < curr.val:
                return curr
            if p.val == curr.val or q.val == curr.val:
                return curr
            if p.val < curr.val and q.val < curr.val:
                return helper(curr.left, p, q)
            else:
                return helper(curr.right, p, q)
        
        return helper(root, p, q)