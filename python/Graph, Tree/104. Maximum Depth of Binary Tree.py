# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Date: Nov 1, 2023
# Difficulty: Easy

from treenode import *
import collections

# Solution 1: BFS
# Time: O(n), Space: O(n)
class Solution1(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                current_root = queue.popleft()
                if current_root.left:
                    queue.append(current_root.left)
                if current_root.right:
                    queue.append(current_root.right)

        return depth

# Solution 2: DFS
# Time: O(n), Space: O(n)
class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, depth):
            if not root:
                return depth
            return max(dfs(root.left, depth+1), dfs(root.right, depth+1))

        return dfs(root, 0)

# Test case
solution = Solution2()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

result = solution.maxDepth(root)
print(result) # 3