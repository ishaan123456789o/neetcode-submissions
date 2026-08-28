# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''res = []
        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)
        postorder(root)
        return res'''
        if not root:
            return []
        stack = []
        stack.append(root)
        seen = set()
        res = []
        while stack:
            curr = stack[-1]
            if curr.left and curr.left not in seen:
                stack.append(curr.left)
                seen.add(curr.left)
            elif curr.right and curr.right not in seen:
                stack.append(curr.right)
                seen.add(curr.right)
            else:
                res.append(curr.val)
                stack.pop()
        return res


        