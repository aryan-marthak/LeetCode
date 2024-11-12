# 160. Intersection of Two Linked Lists

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        temp1 = headA
        temp2 = headB

        if not temp1 and not temp2:
            return null

        while temp1 != temp2:
            if temp1 == None:
                temp1 = headB
            else:
                temp1 = temp1.next
            if temp2 == None:
                temp2 = headA
            else:
                temp2 = temp2.next
        return temp1