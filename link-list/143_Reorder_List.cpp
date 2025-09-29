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
        vector<ListNode*> nodes;
        ListNode * temp  =head;
        
        while(temp!=nullptr){
           nodes.push_back(temp);
           temp = temp->next;
        }


        for(int i =0 ; i < nodes.size();i++){

            nodes[i]->next= nullptr;
        }

        ListNode *prev= nullptr;
        int n = nodes.size();
        if(n==1){return;}
        int i = 0;
        int j = n-1;
        while(i<j){
            nodes[i]->next = nodes[j];
            if(prev !=nullptr)
                prev->next = nodes[i];
            prev = nodes[j];
            i++;
            j--;
        }
        if(n % 2 != 0){
            nodes[j+1]->next = nodes[n/2];
        }
        
    }
};


      
