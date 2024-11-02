# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Date: Nov 1, 2024
# Difficulty: Medium

from treenode import *
# Solution
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        if not root:
            return []
        output = []

        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            level_list = []

            for _ in range(level_size):
                node = queue.popleft()
                level_list.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            output.append(level_list)

        return output

# Test Case
root = [3,9,20,None,None,15,7]
root_treenode = list_to_tree(root)

solution = Solution()
result = solution.levelOrder(root_treenode)
print(result) # True
