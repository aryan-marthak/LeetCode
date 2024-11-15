# 203. Remove Linked List Elements

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        while curr:
            x = curr.next
            if curr.val == val:
                prev.next = x
            else:
                prev = curr
            curr = x
        return dummy.next
