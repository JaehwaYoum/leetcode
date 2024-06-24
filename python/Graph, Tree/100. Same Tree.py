# 100. Same Tree
# https://leetcode.com/problems/same-tree/

# Date: Jun 22, 2024
# Difficulty: Easy

from treenode import *

# Solution
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        # both nodes are None: identical
        if not p and not q:
            return True

        # one of the nodes is None but the other is not: not identical
        if not p or not q:
            return False

        # values of the current nodes are different : not identical
        if p.val != q.val:
            return False

        # recursively check the left and right subtrees
        return (self.isSameTree(p.left, q.left) \
                and self.isSameTree(p.right, q.right))


# Test Case
p = [1,2]; q = [1,None,2]
p_treenode = list_to_tree(p)
q_treenode = list_to_tree(q)

solution = Solution()
result = solution.isSameTree(p_treenode, q_treenode)
print(result) # False