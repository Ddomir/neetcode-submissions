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
    TreeNode* invertTree(TreeNode* root) {
        return recInvTree(root);
    }

    TreeNode* recInvTree(TreeNode* node) {
        if (!node) return nullptr;
        if (!node->left && !node->right) return node;
        TreeNode* temp = node->left;
        node->left = node->right;
        node->right = temp;
        recInvTree(node->left);
        recInvTree(node->right);
        return node;
    }

};
