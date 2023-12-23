# 687. Longest Univalue Path
# https://leetcode.com/problems/longest-univalue-path/

# Date: Dec 23, 2023
# Difficulty: Medium

from treenode import *

# Solution
class Solution(object):
    result = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)
            return max(left, right)

        dfs(root)
        return self.result

# Test case
solution = Solution()

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(5)

result = solution.longestUnivaluePath(root)
print(result) # 2
