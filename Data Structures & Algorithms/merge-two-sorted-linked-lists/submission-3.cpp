/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* listA, ListNode* listB) {
        ListNode dummy;
        ListNode* tail = &dummy;

        while (listA && listB) {
            if (listA->val < listB->val) {
                tail->next = listA;
                listA = listA->next;
            } else {
                tail->next = listB;
                listB = listB->next;
            }
            tail = tail->next;
        }

        tail->next = listA ? listA : listB;
        return dummy.next;
    }
};
