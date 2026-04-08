# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Recurrsion
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

        # Iterative
        
        # temp = ListNode()
        # dummy = temp
        
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         dummy.next = list1
        #         list1 = list1.next
        #     else:
        #         dummy.next = list2
        #         list2 = list2.next
        #     dummy = dummy.next
        # if list1:
        #     dummy.next = list1
        # elif list2:
        #     dummy.next = list2
        # return temp.next
        