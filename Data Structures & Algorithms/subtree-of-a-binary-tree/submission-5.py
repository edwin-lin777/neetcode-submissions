# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def contains(t1, t2):
            if t1 == None and t2 == None:
                return True

            if t1 == None and t2 != None:
                return False
            if t2 == None and t1 != None:
                return False
            if t1.val != t2.val:
                return False
            return contains(t1.left, t2.left) and contains(t1.right, t2.right)

        
        def helper(t1, t2):
            if t1 == None and t2 == None:
                return True
            if t1 == None and t2 is not None:
                return False
        
            if contains(t1, t2) == True:
                return True
             
            return helper(t1.left, t2) or helper(t1.right, t2)
        
        return helper(root, subRoot)
