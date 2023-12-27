# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

# Date: Dec 22, 2023
# Difficulty: Easy

from treenode import *

# Solution 1: BFS
import collections
class Solution1(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)

        return root

# Solution 2: DFS
class Solution2(object):
    def invertTree(self, root):
        stack = collections.deque([root])

        while stack:
            node = stack.pop()

            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
            # node.left, node.right = node.right, node.left

        return root


    # Solution 3: Pythonic
class Solution3(object):
    def invertTree(self, root):
        if root:
            root.left, root.right = \
            self.invertTree(root.right), self.invertTree(root.left)
        return root

# Test case
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

solution = Solution3()
inverted_tree = solution.invertTree(root)
printTree(inverted_tree)