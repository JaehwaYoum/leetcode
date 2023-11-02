# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

# Date: Nov 1, 2023
# Difficulty: Easy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n), Space: O(n), DFS
class Solution(object):
    diameter = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.diameter

# Test case
solution = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result = solution.diameterOfBinaryTree(root)
print(result) # 3