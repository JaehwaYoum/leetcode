# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Date: Nov 1, 2023
# Difficulty: Easy

from treenode import *
import collections

# Solution 1: BFS
# Time: O(n), Space: O(n)
class Solution1(object):
    def maxDepth(self, root: TreeNode) -> int:
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
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(root, depth):
            if not root:
                return depth
            return max(dfs(root.left, depth+1), dfs(root.right, depth+1))

        return dfs(root, 0)

# Solution 3: DFS - 2
class Solution3(object):
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        leftdepth = self.maxDepth(root.left)
        rightdepth = self.maxDepth(root.right)

        return 1 + max(leftdepth, rightdepth) # adding 1 is the parent node of the two subtrees 


# Test case
solution = Solution3()

root = [3,9,20,None,None,15,7]
root_treenode = list_to_tree(root)

result = solution.maxDepth(root_treenode)
print(result) # 3