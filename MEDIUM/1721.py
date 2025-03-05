# 1721. Swapping Nodes in a Linked List

# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        arr[k-1], arr[-k] = arr[-k], arr[k-1]

        dummy = curr = ListNode(0)
        for a in arr:
            curr.next = ListNode(a)
            curr = curr.next
        return dummy.next