# 112. Path Sum

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(node, sum):
            if not node:
                return False
            
            sum += node.val
            if not node.left and not node.right:
                return sum == targetSum
            
            return (dfs(node.left, sum) or dfs(node.right, sum))
        return dfs(root, 0)