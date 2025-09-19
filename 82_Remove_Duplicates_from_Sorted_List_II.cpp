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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *ptr1 = head;
        ListNode *res = nullptr;
        bool isFound = false;

        while(ptr1 != nullptr){
            ListNode *ptr2 = head;
            while(ptr2 != nullptr){
                if(ptr1 != ptr2 && ptr1->val == ptr2->val){
                    isFound = true;

                    break;
                }
                ptr2 = ptr2->next;
            }
            if(!isFound){
                if(res == nullptr){
                    res = new ListNode(ptr1->val);
                    ptr1 = ptr1->next;
                    continue;
                }

                ListNode *temp = res;
                while(temp->next!=nullptr){
                    temp = temp->next;
                }
                temp->next = new ListNode(ptr1->val);
            }
            isFound = false;
            ptr1 = ptr1->next;
        }
        return res;
    } // not the best solution O(n^2) time complexity and space O(n)
};
