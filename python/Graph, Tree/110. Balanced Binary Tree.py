# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

# Date: Nov 1, 2023
# Difficulty: Easy

from treenode import *

# Solution
# Time: O(n), Space: O(n)
class Solution(object):
    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if left == -1 or right == -1 or abs(left-right) >1:
                return -1

            return max(left, right) + 1

        return dfs(root) != -1


# Test case
solution = Solution()
root = [3,9,20,None,None,15,7]
root_treenode = list_to_tree(root)

result = solution.isBalanced(root_treenode)
print(result) # True