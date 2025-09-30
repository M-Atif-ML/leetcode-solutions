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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if(left == right) return head;
        int size = 0;
        ListNode * temp = head;
        while(temp!=nullptr){
            size++;
            temp = temp->next;
        }
        temp = head;
        ListNode ** nodes = new ListNode*[size];
        int i =0 ;
        while(temp!=nullptr){
            nodes[i] = temp;
            i++;
            temp = temp->next; 
        }
        for(int i =0 ; i < size; i++){
            nodes[i]->next = nullptr;
        }
        left--;
        right--;
        ListNode * temp_node =nullptr;
        while(left <= right){
            temp = nodes[left];
            nodes[left] = nodes[right];
            nodes[right]=temp;
            right--;
            left++;
        }

        for(int i =0 ; i < size-1; i++){
            nodes[i]->next = nodes[i+1];
        }

        return nodes[0];

    }
};
