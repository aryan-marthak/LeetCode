# 2487. Remove Nodes From Linked List

# You are given the head of a linked list.

# Remove every node which has a node with a greater value anywhere to the right side of it.

# Return the head of the modified linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # using stack method (linear time complexity)
        
        stack = []
        curr = head
        while curr:
            while stack and curr.val > stack[-1]:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next

        dummy = ListNode()
        curr = dummy
        for i in stack:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next