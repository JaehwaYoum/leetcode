# 112. Path Sum 
# 

# Date: Jun 22, 2024
# Difficulty: Easy

from treenode import *

# Solution
class Solution(object):
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)

        return left_sum or right_sum


# Test case
solution = Solution()

root = [5,4,8,11,None,13,4,7,2,None,None,None,1]; targetSum = 22
root_treenode = list_to_tree(root)

result = solution.hasPathSum(root_treenode, targetSum)
print(result) # True
