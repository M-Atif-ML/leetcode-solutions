class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if(!root) return {};
        queue<TreeNode*> q;
        vector<vector<int>> res;
        vector<int> temp;

        q.push(root);
        bool flag = 0;
        while(!q.empty()){
            int n= q.size();
            for(int i=0; i < n;i++){
                TreeNode * node= q.front();
                q.pop();
                temp.push_back(node->val);

  
                if(node->left)
                    q.push(node->left);
                if(node->right)
                    q.push(node->right);
               
            } 
    
            res.push_back(temp);
            temp.clear();
        }


        for (int i = 0; i < res.size();i++){
            if (i % 2 != 0){
                reverse(res[i].begin(), res[i].end());
            }
        }

        return res;
    }
};
