# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/description/

# Date: Nov 1, 2024
# Difficulty: Medium

from treenode import *
class Solution(object):
    def isValidBST(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        output = []
        self._inorder_traversel(root, output)

        for i in range(len(output)-1):
            if output[i] >= output[i+1]:
                return False
        return True

    def _inorder_traversel(self, root: TreeNode, output: list):
        if not root:
            return

        self._inorder_traversel(root.left, output)
        output.append(root.val)
        self._inorder_traversel(root.right, output)


# Test case
solution = Solution()
root = [5,1,4,None,None,3,6]
root_treenode = list_to_tree(root)

result = solution.isValidBST(root_treenode)
print(result)