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
    void pathSum(TreeNode * root, int targetSum,vector <int> temp,vector<vector<int>>&res,int sum){
        if(root == nullptr)
            return;
        sum += root->val;
        temp.push_back(root->val);
        if(sum == targetSum && (!root->left && !root->right)){
            res.push_back(temp);
            return;
        }
        
        pathSum(root->left,targetSum,temp,res,sum);
       
        pathSum(root->right,targetSum,temp,res,sum);
        

    }
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        if(!root) return {};

        vector<vector<int>> res;
        vector<int> temp;

        pathSum(root,targetSum,temp,res,0);

        return res;
    }
};
