# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pArr = []
        qArr = []

        def rootToNode(toFind, node, arr):
            if node:
                arr.append(node)
                if node.val == toFind.val:
                    return arr
                
                if node.val > toFind.val:
                    return rootToNode(toFind, node.left, arr)
                else:
                    return rootToNode(toFind, node.right, arr)
            return None
        
        rootToNode(p, root, pArr)
        rootToNode(q, root, qArr)

        for n in pArr: print(n.val)
        print()
        for n in qArr: print(n.val)

        i = 0
        shortestLen = min(len(pArr), len(qArr)) - 1
        while i <= shortestLen and pArr[i].val == qArr[i].val:
            prevAnc = pArr[i]
            i += 1
        return pArr[i - 1]
