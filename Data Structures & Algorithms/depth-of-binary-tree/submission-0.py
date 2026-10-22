# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0

        def maxHelper(node, depth):
            if node:
                maxHelper(node.left, depth + 1)
                maxHelper(node.right, depth + 1)
                self.maxDepth = max(self.maxDepth, depth)
        
        maxHelper(root, 1)
        return self.maxDepth