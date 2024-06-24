# 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Date: Jun 22, 2024
# Difficulty: Easy


from treenode import *

# Solution
class Solution(object):
    def postorderTraversal(self, root: TreeNode) -> list:
        result = []
        self._postorder_traversal(root, result)
        return result

    def _postorder_traversal(self, node: TreeNode, result: list):
        if node is None:
            return
        self._postorder_traversal(node.left, result)
        self._postorder_traversal(node.right, result)
        result.append(node.val)


# Test case
solution = Solution()
root = [1,2,3]
root_treenode = list_to_tree(root)

result = solution.postorderTraversal(root_treenode)
print(result)