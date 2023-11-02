# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

# Date: Nov 1, 2023
# Difficulty: Easy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(n), Space: O(n)
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

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

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

result = solution.isBalanced(root)
print(result) # 3