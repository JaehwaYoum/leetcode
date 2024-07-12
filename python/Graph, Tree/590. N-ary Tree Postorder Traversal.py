# 590. N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

# Date: Jun 23, 2024
# Difficulty: Easy

from node import *
# Solution
class Solution(object):
    def postorder(self, root: Node) -> list:
        return []


# Test Case
root = [1,None,3,2,4,None,5,6]
root_node = list_to_tree(root)

solution = Solution()
result = solution.postorder(root_node)
print(result) # True
