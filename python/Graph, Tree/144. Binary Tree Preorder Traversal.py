# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Date: Jun 22, 2024
# Difficulty: Easy


from treenode import *

# Solution
class Solution(object):
    def preorderTraversal(self, root: TreeNode) -> list:

        result = []
        self._preorder_traversal(root, result)
        return result

    def _preorder_traversal(self, node: TreeNode, result: list):

        if node is None:
            return

        result.append(node.val)
        self._preorder_traversal(node.left, result)
        self._preorder_traversal(node.right, result)


# Test case
solution = Solution()
root = [1,2,3]
root_treenode = list_to_tree(root)

result = solution.preorderTraversal(root_treenode)
print(result)