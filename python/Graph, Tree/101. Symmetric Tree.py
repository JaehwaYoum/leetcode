# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

# Date: Jun 22, 2024
# Difficulty: Easy

from treenode import *
# Solution
class Solution(object):
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return False

        # initiate a stack and append a tuple of left and right nodes
        stack = []
        stack.append((root.left, root.right))

        while stack:
            left, right = stack.pop()

            # below is the same logic as # 100. Same Tree
            # both nodes are None: identical
            if left is None and right is None:
                return True
            # one of the nodes is None but the other is not: not identical
            if left is None or right is None:
                return False
            # values of the current nodes are different : not identical
            if left.val != right.val:
                return False

            # append to the stack for symmetry check
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

        return True


# Test Case
root = [1,2,2,3,4,4,3]
root_treenode = list_to_tree(root)

solution = Solution()
result = solution.isSymmetric(root_treenode)
print(result) # True
