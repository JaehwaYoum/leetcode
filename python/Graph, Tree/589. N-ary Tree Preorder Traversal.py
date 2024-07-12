# 589. N-ary Tree Preorder Traversal
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

# Date: Jun 23, 2024
# Difficulty: Easy

from node import *
# Solution
class Solution(object):
    def preorder(self, root: Node) -> list:
        result = []
        self._preorder(root, result)
        return result

    def _preorder(self, node, result):
        if node is None:
            return

        result.append(node.val)
        for child in node.children:
            self._preorder(child, result)


# Test Case
root = [1,None,3,2,4,None,5,6]
root_node = list_to_tree(root)

solution = Solution()
result = solution.preorder(root_node)
print(result) # True
