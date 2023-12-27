# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Date: Dec 27, 2023
# Difficulty: Medium

from treenode import *

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            # find the first item in preorder list in the inorder list
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[:index])
            node.right = self.buildTree(preorder, inorder[index+1:])

            return node


# Test case
solution = Solution()
preorder = [3,9,20,15,7]; inorder = [9,3,15,20,7]


result = solution.buildTree(preorder, inorder)
printTree(result)

