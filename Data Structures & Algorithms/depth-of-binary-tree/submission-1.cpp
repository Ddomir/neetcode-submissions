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
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        return max(recMaxDepth(root->left, 1), recMaxDepth(root->right, 1));
    }

    int recMaxDepth(TreeNode* node, int currDepth) {
        if (!node) return currDepth;
        return max(recMaxDepth(node->left, currDepth+1), 
                   recMaxDepth(node->right, currDepth+1));
    }
};
