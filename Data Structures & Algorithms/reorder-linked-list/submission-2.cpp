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
    void reorderList(ListNode* head) {
        // 1st pass, get length
        int count = 0;
        for (ListNode* curr = head; curr; curr = curr->next) count++;

        // 2nd pass, reverse 2nd half
        ListNode* mid = head;
        for (int i = 0; i < count / 2; i++) mid = mid->next;
        
        ListNode* curr = mid->next;
        ListNode* prev = nullptr;
        mid->next = nullptr;

        while (curr) {
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        ListNode* first = head;
        ListNode* second = prev;

        // 3rd pass, zipper merge
        while (second) {
            ListNode* firstNext = first->next;
            ListNode* secondNext = second->next;
            first->next = second;
            second->next = firstNext;
            first = firstNext;
            second = secondNext;
        }
    }
};
