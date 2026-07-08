# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """res = []
        def traverse(node, parent, side):
            if not node:
                return
            if not parent or side == "right":
                res.append(node.val)
            elif side == "left" and not parent.right:
                res.append(node.val)
            if not node.right and not node.left:
                return
            if node.right:
                traverse(node.right, node, "right")
            if node.left:
                traverse(node.left, node, "left")
        traverse(root, None, None)
        return res"""
        
        if not root:
            return []
        levels = []
        q = deque()
        q.append(root)
        while q:
            currLevel = []
            for _ in range(len(q)):
                currNode = q.popleft()
                currLevel.append(currNode.val)
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            if currLevel:
                levels.append(currLevel)
        res = []
        for level in levels:
            res.append(level[-1])
        return res
            