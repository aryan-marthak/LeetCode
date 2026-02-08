# 110. Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            lhs = dfs(node.left)
            if lhs == -1:
                return -1
            rhs = dfs(node.right)
            if rhs == -1:
                return -1
            if abs(rhs - lhs) > 1:
                return -1
            return max(lhs, rhs) + 1
        return dfs(root) != -1