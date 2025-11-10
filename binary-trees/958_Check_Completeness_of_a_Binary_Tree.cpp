class Solution {
public:
    bool isCompleteTree(TreeNode* root) {
        queue<TreeNode *> q;
        q.push(root);
        bool isNull = false;

        while(!q.empty()){
            TreeNode * curr = q.front();
            q.pop();
            if(curr){
                q.push(curr->left);
                q.push(curr->right);
            }
            else{
                while(!q.empty()){
                    if(q.front()) return false;
                    q.pop();
                }
            }
       
           
        }

        return true;

    }
};
