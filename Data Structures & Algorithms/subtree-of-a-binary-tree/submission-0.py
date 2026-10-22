# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def findSubRoot(node):
            if node:
                if node.val == subRoot.val:
                    if checkEq(node, subRoot):
                        return True
                return (findSubRoot(node.left) or findSubRoot(node.right))
            return False
                

        def checkEq(node, subNode):
            if not node and not subNode:
                return True
            if node and subNode and node.val == subNode.val:
                return checkEq(node.left, subNode.left) and checkEq(node.right, subNode.right)
            else:
                return False

        
        return findSubRoot(root)
        