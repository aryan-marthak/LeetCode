# 1325. Delete Leaves With a Given Value

# Given a binary tree root and an integer target, delete all the leaf nodes with value target.

# Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def checkleaf(node):
            if node:
                if not node.left and not node.right:
                    return True
                else:
                    return False
        
        if not root:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if root and root.val == target:
            if checkleaf(root):
                return None
        
        return root