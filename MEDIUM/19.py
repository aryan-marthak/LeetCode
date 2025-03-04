# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p1 = head
        p2 = dummy
        count = 0
        while p1:
            p1 = p1.next
            count += 1
            if count > n:
                p2 = p2.next
        p2.next = p2.next.next
        return dummy.next
    
    # MY OWN METHOD
    
        dummy = ListNode(0, head)
        temp = dummy
        Len = 0
        while temp.next:
            Len += 1
            temp = temp.next
        
        Index = Len - n

        p1 = dummy
        for i in range(Index):
            p1 = p1.next
        p1.next = p1.next.next
        return dummy.next