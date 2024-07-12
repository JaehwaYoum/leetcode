# 429. N-ary Tree Level Order Traversal
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

# Date: Jun 23, 2024
# Difficulty: Easy

from node import *
# Solution
class Solution(object):
    def levelOrder(self, root: Node) -> list:
        result = []
        self._level_order(root, 0, result)
        return result

    def _level_order(self, node, level, result):
        if node is None:
            return

        if len(result) == level:
            result.append([])

        result[level].append(node.val)
        for child in node.children:
            self._level_order(node, level+1, result)



# Test Case
root = [1,None,3,2,4,None,5,6]
root_node = list_to_tree(root)

solution = Solution()
result = solution.levelOrder(root_node)
print(result) # True
