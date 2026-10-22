# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        if not curr1:
            return curr2
        if not curr2:
            return curr1

        if curr1.val < curr2.val:
            newList = curr1
            curr1 = curr1.next
        else:
            newList = curr2
            curr2 = curr2.next
        
        newHead = newList

        while curr1 and curr2:
            print(newList.val)
            if curr1.val < curr2.val:
                newList.next = curr1
                newList = newList.next
                curr1 = curr1.next
            else:
                newList.next = curr2
                newList = newList.next
                curr2 = curr2.next
        
        if curr1:
            newList.next = curr1
        else:
            newList.next = curr2
    
        return newHead
