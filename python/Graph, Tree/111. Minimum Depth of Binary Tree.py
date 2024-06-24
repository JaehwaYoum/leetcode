# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Date: Jun 22, 2024
# Difficulty: Easy

from treenode import *
# Solution
class Solution(object):
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        # calculate the depth of left and right subtrees
        # if there is no right or left child, consider it as having infinite depth
        left_depth = self.minDepth(root.left) if root.left else float('inf')
        right_depth = self.minDepth(root.right) if root.right else float('inf')

        return 1 + min(left_depth, right_depth) # adding 1 is the parent node of the two subtrees


# Test case
solution = Solution()

root = [3,9,20,None,None,15,7]
root_treenode = list_to_tree(root)

result = solution.minDepth(root_treenode)
print(result) # 2