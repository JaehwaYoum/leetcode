# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/

# Date: Jun 22, 2024
# Difficulty: Easy

from treenode import *
# Solution
class Solution(object):
    def binaryTreePaths(self, root: TreeNode) -> list:
        result = []
        self._binary_tree_path(root, "", result)
        return result

    def _binary_tree_path(self, node, path, result):

        if node is None:
            return
        path += str(node.val)

        if node.left is None and node.right is None:
            result.append(path)

        else:
            self._binary_tree_path(node.left, path + "->", result)
            self._binary_tree_path(node.right, path + "->", result)


# Test case
solution = Solution()
root = [1,2,3,None,5]
root_treenode = list_to_tree(root)

result = solution.binaryTreePaths(root_treenode)
print(result) # ["1->2->5","1->3"]