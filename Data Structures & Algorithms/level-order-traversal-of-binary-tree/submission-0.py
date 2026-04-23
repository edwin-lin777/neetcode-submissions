# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final = []
        q = collections.deque()
        q.append(root)
        while q:
            qLen = len(q)
            temp = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    val = node.val
                    temp.append(val)
                    q.append(node.left)
                    q.append(node.right)
            if temp:
                final.append(temp)
        return final

         
        