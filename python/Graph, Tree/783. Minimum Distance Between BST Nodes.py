# 783. Minimum Distance Between BST Nodes
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
import sys

# Date: Dec 27, 2023
# Difficulty: Easy

from treenode import *

# Solution 1: recursive
class Solution1(object):
    prev = -sys.maxsize
    result = sys.maxsize

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result


# Solution 2: DFS
class Solution2(object):
    def minDiffInBST(self, root):
        prev = -sys.maxsize
        result = sys.maxsize
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result = min(result, node.val - prev)
            prev = node.val

            node = node.right
        return result

# Test case
solution = Solution2()

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(6)

result = solution.minDiffInBST(root)
print(result)
