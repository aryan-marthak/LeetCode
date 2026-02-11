# 1382. Balance a Binary Search Tree

# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node, array):
            if not node:
                return
            inorder(node.left, array)
            array.append(node.val)
            inorder(node.right, array)
        
        def build(array, l, r):
            if l > r:
                return None
            mid = l + (r - l) // 2
            node = TreeNode(array[mid])
            node.left = build(array, l, mid - 1)
            node.right = build(array, mid + 1, r)
            return node

        array = []
        inorder(root, array)
        return build(array, 0, len(array) - 1)