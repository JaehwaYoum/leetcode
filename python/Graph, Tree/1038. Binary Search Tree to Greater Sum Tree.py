# 1038. Binary Search Tree to Greater Sum Tree
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Date: Dec 27, 2023
# Difficulty: Medium

from treenode import *

# Solution
class Solution(object):
    val = 0

    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root

# Test case
solution = Solution()

root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)

root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

result = solution.bstToGst(root)
print(tree_to_list(result)) # [30, 36, 36, 35, 33, 21, 26, 15, 8]
