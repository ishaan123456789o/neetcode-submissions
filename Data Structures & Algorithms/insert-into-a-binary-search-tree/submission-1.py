# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode()
            root.val = val
            return root
        def getAllNodes(node, path):
            if not node:
                return
            path.append(node.val)
            getAllNodes(node.left, path)
            getAllNodes(node.right, path)           
        def traverse(node, val):
            if val < node.val:
                if node.left:
                    if val > node.left.val:
                        left = node.left
                        node.left = TreeNode()
                        node.left.val = val
                        nodes = []
                        getAllNodes(left, nodes)
                        for value in nodes:
                            traverse(node.left, value)
                        return
                    else:
                        traverse(node.left, val)
                else:
                    node.left = TreeNode()
                    node.left.val = val
                    return
            elif val > node.val:
                if node.right:
                    if val < node.right.val:
                        right = node.right
                        node.right = TreeNode()
                        node.right.val = val
                        nodes = []
                        getAllNodes(right, nodes)
                        for value in nodes:
                            traverse(node.right, value)
                        return
                    else:
                        traverse(node.right, val)
                else:
                    node.right = TreeNode()
                    node.right.val = val
                    return
        traverse(root, val)
        return root
                
        