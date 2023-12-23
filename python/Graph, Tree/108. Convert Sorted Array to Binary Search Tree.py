# 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Date: Dec 23, 2023
# Difficulty: Easy

from treenode import *

# Solution
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) // 2

        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node

# Test case
solution = Solution()

nums = [-10,-3,0,5,9]
result_tree = solution.sortedArrayToBST(nums)
result = tree_to_list(result_tree)
print(result) # [0, -3, -10, 9, 5]