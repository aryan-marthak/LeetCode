# 450. Delete Node in a BST

# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

#     Search for a node to remove.
#     If the node is found, delete the node.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # DETAILED EXPLANATION:
        
        if not root:
            return None
        if root.val == key:
            return self.helper(root)
        cur = root
        while root:
            if key < root.val:
                if root.left and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                root = root.right
        return cur

    def helper(self, root):
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        left = root.left
        right = root.right
        while left.right:
            left = left.right
        left.right = right
        return root.left
        
        #  SIMPLER EXPLANATION:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)

        return root