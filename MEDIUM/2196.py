# 2196. Create Binary Tree From Descriptions

# You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

#     If isLefti == 1, then childi is the left child of parenti.
#     If isLefti == 0, then childi is the right child of parenti.

# Construct the binary tree described by descriptions and return its root.

# The test cases will be generated such that the binary tree is valid.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent, child, is_left in descriptions:
            children.add(child)
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if is_left:
                nodes[parent].left = nodes[child]
            if not is_left:
                nodes[parent].right = nodes[child]
        
        for p, c, l in descriptions:
            if p not in children:
                return nodes[p]