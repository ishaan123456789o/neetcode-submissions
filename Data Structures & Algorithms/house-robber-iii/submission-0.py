# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(node):
            if node not in memo:
                memo[node] = node.val
                if node.left:
                    if node.left.left:
                        memo[node] += dp(node.left.left)
                    if node.left.right:
                        memo[node] += dp(node.left.right)
                if node.right:
                    if node.right.left:
                        memo[node] += dp(node.right.left)
                    if node.right.right:
                        memo[node] += dp(node.right.right)
                if node.right and node.left:
                    memo[node] = max(memo[node], dp(node.right) + dp(node.left))
                elif node.right:
                    memo[node] = max(memo[node], dp(node.right))
                elif node.left:
                    memo[node] = max(memo[node], dp(node.left))
            return memo[node]
        return dp(root)

        