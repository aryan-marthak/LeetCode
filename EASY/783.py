# 783. Minimum Distance Between BST Nodes

# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, res = None, float("inf")

        def dfs(node):
            nonlocal prev, res
            if not node:
                return
            
            dfs(node.left)
            if prev:
                res = min(res, node.val - prev.val)
            prev = node
            dfs(node.right)

        dfs(root)
        return res