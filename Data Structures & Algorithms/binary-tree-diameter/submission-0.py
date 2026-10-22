# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0

        def diamHelper(node):
            nonlocal maxDiam
            
            if not node:
                return 0
            
            left = diamHelper(node.left)
            right = diamHelper(node.right)
            maxDiam = max(maxDiam, left + right)
            return max(left, right) + 1

        diamHelper(root)
        return maxDiam