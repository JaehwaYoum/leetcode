# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

# Date: Dec 22, 2023
# Difficulty: Easy

from treenode import *
import collections

# Solution 1: BFS (queue)
class Solution1(object):
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)

        return root

# Solution 2: DFS (stack)
class Solution2(object):
    def invertTree(self, root: TreeNode) -> TreeNode:
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
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = \
            self.invertTree(root.right), self.invertTree(root.left)
        return root


# Test case
solution = Solution3()
root = [4,2,7,1,3,6,9]
root_treenode = list_to_tree(root)

inverted_tree = solution.invertTree(root_treenode)
printTree(inverted_tree)