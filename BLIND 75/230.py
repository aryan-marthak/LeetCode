# 230. Kth Smallest Element in a BST

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def helper(node):
            if not node:
                return
            res.append(node.val)
            helper(node.left)
            helper(node.right)
        
        helper(root)
        res.sort()
        return res[k - 1]