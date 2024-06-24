# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Date: Jun 22, 2024
# Difficulty: Easy

from treenode import *

# Solution
class Solution(object):
    def inorderTraversal(self, root: TreeNode) -> list:
        result = []
        self._inorder_traversal(root, result)
        return result

    def _inorder_traversal(self, node: TreeNode, result: list):
        if node is None:
            return
        self._inorder_traversal(node.left, result)
        result.append(node.val)
        self._inorder_traversal(node.right, result)


# Test case
solution = Solution()
root = [1,2,3]
root_treenode = list_to_tree(root)

result = solution.inorderTraversal(root_treenode)
print(result)