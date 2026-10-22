# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        first, second = head, dummy

        # Move first to n
        for _ in range(n):
            first = first.next
        
        # Move both until first is at end
        # Second will be one before n from end
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next

