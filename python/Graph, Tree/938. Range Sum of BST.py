# 938. Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/

# Date: Dec 27, 2023
# Difficulty: Easy

from treenode import *

# Solution 1: Brute-force
class Solution1(object):
    result = 0

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """

        if not root:
            return 0

        if root.val >= low and root.val <= high:
            self.result += root.val

        self.rangeSumBST(root.left, low, high)
        self.rangeSumBST(root.right, low, high)

        return self.result


# Solution 2: DFS with branch pruning
class Solution2(object):
    def rangeSumBST(self, root, low, high):
        def dfs(node):
            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)


# Solution 3: DFS
class Solution3(object):
    def rangeSumBST(self, root, low, high):
        stack, sum = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum

# Solution 4: BFS
class Solution4(object):
    def rangeSumBST(self, root, low, high):
        queue, sum = [root], 0
        while queue:
            node = queue.pop(0)
            if node:
                if node.val > low:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum

# Test case
solution = Solution4()

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right = TreeNode(15)
root.right.right = TreeNode(18)

low = 7; high = 16
result = solution.rangeSumBST(root, low, high)
print(result) # 32
