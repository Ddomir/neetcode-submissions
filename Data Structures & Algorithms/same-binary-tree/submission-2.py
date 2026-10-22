# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            # If both exist
            if p and q and p.val == q.val:
                left = dfs(p.left, q.left)
                right = dfs(p.right, q.right)
                # If left and right children pairs are equal
                if left and right:
                    return True
                return False

            # If both None
            elif not p and not q:
                return True
            
            # Mismatch, false
            return False
        
        return dfs(p, q)
            