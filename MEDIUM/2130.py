# 2130. Maximum Twin Sum of a Linked List

# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

#     For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.

# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        mid = end = head
        while end.next and end.next.next:
            end = end.next.next
            mid = mid.next
        p2 = mid
        prev = None
        while p2:
            p2next = p2.next
            p2.next = prev
            prev = p2
            p2 = p2next
        p2.next = prev

        final = 0
        p1 = head
        while p1 and p2:
            Sum = p1.val + p2.val
            final = max(Sum , final)
            p1 = p1.next
            p2 = p2.next
        return final