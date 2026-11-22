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
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        // 1st pass - get sz
        int sz = 0;
        for (ListNode* curr = head; curr; curr = curr->next) sz++;

        // 2nd pass - get to n-1, point its next to n+1
        ListNode dummy(0, head);
        ListNode* prev = &dummy;
        for (int i = 0; i < sz - n; i++) prev = prev->next;

        prev->next = prev->next->next;
        return dummy.next;
    }
};
