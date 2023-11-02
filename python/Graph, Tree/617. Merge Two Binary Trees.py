# 617. Merge Two Binary Trees
# https://leetcode.com/problems/merge-two-binary-trees/

# Date: Nov 1, 2023
# Difficulty: Easy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: recursive
# Time: O(n), Space: O(n)
class Solution1(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """

        if not (root1 and root2):
            return root1 or root2
        else:
            result = TreeNode(root1.val + root2.val)
            result.left = self.mergeTrees(root1.left, root2.left)
            result.right = self.mergeTrees(root1.right, root2.right)

        return result

# Solution 2: BFS
# Time: O(n), Space: O(n)
class Solution2(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """

        if not (root1 and root2):
            return root1 or root2

        queue1, queue2 = collections.deque([root1]), collections.deque([root2])
        while queue1 and queue2:
            node1, node2 = queue1.popleft(), queue2.popleft()

            if node1 and node2:
                node1.val = node1.val + node2.val

                if (not node1.left) and node2.left:
                    node1.left = TreeNode(0)
                if (not node1.right) and node2.right:
                    node1.right = TreeNode(0)

                queue1.append(node1.left)
                queue1.append(node1.right)
                queue2.append(node2.left)
                queue2.append(node2.right)

        return root1

# Print Tree
import collections
def printTree(root):
    if not root:
        return
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Test case
solution = Solution1()
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

merged_tree = solution.mergeTrees(root1, root2)
printTree(merged_tree)