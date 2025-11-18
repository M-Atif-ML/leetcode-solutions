/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isEven(int val){
        return (val%2==0);
    }
    bool isEvenOddTree(TreeNode* root) {
        int index =0 ;
        int size_=0;
        TreeNode * temp1=nullptr;
        int temp2= root->val;
        vector<int> arr;
        queue<TreeNode*> q;
        q.push(root);
        
        while(!q.empty()){
            
            size_ = q.size();
       
            for(int i= 0 ; i< size_;i++){
                temp1 = q.front();
               
                q.pop();
                arr.push_back(temp1->val);
                if(index%2==0){
                    if(isEven(temp1->val) )
                        return false;
                }
                else{
                    if(!isEven(temp1->val)  ){
                        return false;
                    }
                }
            

                if(temp1->left) q.push(temp1->left);
                if(temp1->right) q.push(temp1->right);
                
            }

            for(int i =0 ;i < arr.size()-1;i++){
                if(index%2==0 && (arr[i] >= arr[i+1])){
                    return false;
                }
                if(index%2!=0 && (arr[i] <= arr[i+1])){
                    return false;
                }
                
            }
            index++;
            arr.clear();
        }

        return true;
    }
};
