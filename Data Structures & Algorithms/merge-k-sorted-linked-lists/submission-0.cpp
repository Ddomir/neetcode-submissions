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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return nullptr;

        while (lists.size() > 1) {
            vector<ListNode*> joined;
            for (int j = 0; j < lists.size(); j += 2) { // traverse log n groups
                ListNode* b = (j + 1 < lists.size()) ? lists[j+1] : nullptr;
                joined.push_back(merge2Lists(lists[j], b));
            }
            lists = joined;
        }
        return lists[0];
    }

    ListNode* merge2Lists(ListNode* listA, ListNode* listB) {
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
