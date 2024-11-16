# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Itterative way of doing this

class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


