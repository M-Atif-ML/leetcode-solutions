class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<int, vector<int>, greater<int>> minHeap;
      

        for(int i =0 ; i < lists.size();i++){
            ListNode * temp = lists[i];
        
            
            while(temp!=nullptr){   
                minHeap.push(temp->val);
                temp = temp->next;
            }
        }
        ListNode * resHead = new ListNode();
        ListNode* resTail = resHead;
        while(!minHeap.empty()){
     
            resTail->next = new ListNode(minHeap.top());
            minHeap.pop();
            resTail = resTail->next;
        }

        return resHead->next;
    }
};
