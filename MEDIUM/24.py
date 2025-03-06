# 24. Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            next_to_next = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = next_to_next
            prev.next = second

            prev = curr
            curr = next_to_next
        return dummy.next