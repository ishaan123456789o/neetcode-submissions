# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        parents={}
        parents[root] = (None, None)
        res = root
        def traverse(node):
            if not node.left and not node.right:
                return
            if node.left:
                parents[node.left] = (node, "left")
                traverse(node.left)
            if node.right:
                parents[node.right] = (node, "right")
                traverse(node.right)
        def solution(node):
            nonlocal res
            if not node.right and not node.left:
                if node.val == target:
                    parentTup = parents[node]
                    parent = parentTup[0]
                    dir = parentTup[1]
                    if not parent:
                        res = None
                    else:
                        if dir == "right":
                            parent.right = None
                        elif dir == "left":
                            parent.left = None
                        if not parent.right and not parent.left:
                            solution(parent)
            if node.right:
                solution(node.right)
            if node.left:
                solution(node.left)
            return
        
        traverse(root)
        solution(root)
        return res

        