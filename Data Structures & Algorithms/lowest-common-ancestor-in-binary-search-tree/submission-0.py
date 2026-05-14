# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None
        def traverse(node):
            nonlocal res
            if not node:
                return
            if (p.val < node.val and q.val > node.val) or (p.val > node.val and q.val < node.val):
                res = node
                return
            if p.val == node.val or q.val == node.val:
                res = node
                return
            if p.val < node.val and q.val < node.val:
                traverse(node.left)
            if p.val > node.val and q.val > node.val:
                traverse(node.right)
        traverse(root)
        return res
        