# 102. Binary Tree Level Order Traversal

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        next_q = []
        level = []
        res = []
        while q:
            for i in q:
                level.append(i.val)
                if i.left:
                    next_q.append(i.left)
                if i.right:
                    next_q.append(i.right)
            res.append(level)
            level = []
            q = next_q
            next_q = []
        return res