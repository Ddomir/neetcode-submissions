# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumStr1 = sumStr2 = ""

        while l1:
            sumStr1 = str(l1.val) + sumStr1
            l1 = l1.next
        
        while l2:
            sumStr2 = str(l2.val) + sumStr2
            l2 = l2.next
        
        total = str(int(sumStr1) + int(sumStr2))

        resHead = ListNode(total[-1]) # first char
        resCurr = resHead
        
        for c in reversed(total[:-1]):
            resCurr.next = ListNode(c)
            resCurr = resCurr.next


        return resHead