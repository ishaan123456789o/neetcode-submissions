# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(n1, n2):
            if (not n1 and n2) or (not n2 and n1):
                return False
            if not n1 and not n2:
                return True
            if n1.val != n2.val:
                return False
            if traverse(n1.left, n2.left) and traverse(n1.right, n2.right):
                return True
            else:
                return False
        return traverse(p, q)