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
    vector<TreeNode*> generateTrees(int n) {
        if (n <= 0) {
            return {};
        }
        return buildTrees(1, n);
    }

private:
    vector<TreeNode*> buildTrees(int start, int end) {
        if (start > end) {
            return {nullptr};
        }
        vector<TreeNode*> allTrees;

        for (int rootVal = start; rootVal <= end; ++rootVal) {
            vector<TreeNode*> leftSubtrees = buildTrees(start, rootVal-1);
            vector<TreeNode*> rightSubtrees = buildTrees(rootVal+1, end);

            for (TreeNode* left : leftSubtrees) {
                for (TreeNode* right : rightSubtrees) {
                    TreeNode* root = new TreeNode(rootVal, left, right);
                    allTrees.push_back(root);
                }
            }
        }

        return allTrees;
    }
};