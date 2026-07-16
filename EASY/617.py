# 617. Merge Two Binary Trees

# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node1, node2):
            if not node1:
                return node2
            if not node2:
                return node1
            node1.val += node2.val
            node1.left = helper(node1.left, node2.left)
            node1.right = helper(node1.right, node2.right)

            return node1
        return helper(root1, root2)
    
        # def helper(node1, node2):
        #     if not node1 and not node2:
        #         return None

        #     v1 = node1.val if node1 else 0
        #     v2 = node2.val if node2 else 0

        #     root = TreeNode(v1 + v2)
        #     root.left = helper(node1.left if node1 else None, node2.left if node2 else None)
        #     root.right = helper(node1.right if node1 else None, node2.right if node2 else None)

        #     return root
        # return helper(root1, root2)