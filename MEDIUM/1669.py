# 1669. Merge In Between Linked Lists

# You are given two linked lists: list1 and list2 of sizes n and m respectively.

# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

# The blue edges and nodes in the following figure indicate the result:

# Build the result list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        end = list1
        i = 0

        while i < a - 1:
            end = end.next
            i += 1

        start = end
        while i <= b:
            end = end.next
            i += 1
        start.next = list2

        while list2.next:
            list2 = list2.next
        list2.next = end
        return list1