/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void flatten(TreeNode* root) {
        if(!root)
            return;
        stack<TreeNode*> st;
        while(root)
        {
            if(root->left)
            {
                if(root->right)
                    st.push(root->right);
                root->right = root->left;
                root->left = NULL;
            }
            if(!root->right && !st.empty())
            {
                root->right = st.top();
                st.pop();
            }
            root = root->right;
        }
        
    }
};
