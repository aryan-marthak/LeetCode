# 404. Sum of Left Leaves

# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0
            total = 0
            if isLeafNode(root.left):
                total += root.left.val
            total += helper(root.left)
            total += helper(root.right)
            return total
        def isLeafNode(root):
            if not root:
                return False
            if not root.left and not root.right:
                return True
            else:
                return False
        return helper(root)