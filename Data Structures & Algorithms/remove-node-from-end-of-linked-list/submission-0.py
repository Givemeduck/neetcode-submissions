# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #two pointers, r = n
        #singly, so can only move left pointer to the left
        dummy = ListNode(0) #this initializes a dummy node before the start of the linked list
        #

        dummy.next = head  #initializing the head? i thought the problem made it clear what and where the head was
        l, r= dummy, dummy
        
        for i in range(n):
            r = r.next
        
        while r.next:
            l = l.next
            r = r.next

        l.next = l.next.next

        return dummy.next
        
        #l will be on the target number that we want to delete