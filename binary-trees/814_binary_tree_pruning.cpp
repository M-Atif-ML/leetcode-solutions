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
    bool helper(TreeNode * root){
        if(!root) return false;

        if(root->val == 1){
            return true;
        }

        return helper(root->left)||helper(root->right);
    }
    void dfs(TreeNode * root){
        if(!root) return;
        if(!helper(root->left))
            root->left=nullptr;
        if(!helper(root->right))
            root->right=nullptr;
        

        dfs(root->left);
        dfs(root->right);


    }
    TreeNode* pruneTree(TreeNode* root) {
        if(!helper(root)) return nullptr;

        dfs(root);

        return root;
    }
};
