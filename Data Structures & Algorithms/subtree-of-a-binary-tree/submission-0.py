# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(r1, r2):
            if not r1 and not r2:
                return True
            if (r1.left and not r2.left) or (r2.left and not r1.left):
                return False
            if (r1.right and not r2.right) or (r2.right and not r1.right):
                return False
            if r1.val != r2.val:
                return False
            return sametree(r1.left, r2.left) and sametree(r1.right, r2.right)
        def traverse(node):
            if not node:
                return False
            if node.val == subRoot.val:
                return sametree(node, subRoot) or traverse(node.left) or traverse(node.right)
            return traverse(node.left) or traverse(node.right)
        return traverse(root)