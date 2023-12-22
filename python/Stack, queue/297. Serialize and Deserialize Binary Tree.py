# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
import collections

# Date: Dec 13, 2023
# Difficulty: Hard

# Definition of Binary Tree Node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: queue
class Codec:
    def serialize(self, root):
        queue = collections.deque([root])
        result = []

        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append('#')

        return ' '.join(result)

    def deserialize(self, data):
        if data == '#':
            return None

        nodes = data.split()
        root = TreeNode(int(nodes[0]))
        queue = collections.deque([root])
        index = 1

        while queue:
            node = queue.popleft()
            if nodes[index] != '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            if nodes[index] != '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root

# Solution 2: recursive
class Codec2:
    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')

        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()

# Test Case
# Create the input tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = None
root.left.right = None
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

# Serialize and deserialize the tree
codec = Codec2()
serialized_tree = codec.serialize(root)
deserialized_root = codec.deserialize(serialized_tree)
print(serialized_tree)

# Check if the deserialized tree matches the original tree
assert deserialized_root.val == 1
assert deserialized_root.left.val == 2
assert deserialized_root.right.val == 3
assert deserialized_root.left.left is None
assert deserialized_root.left.right is None
assert deserialized_root.right.left.val == 4
assert deserialized_root.right.right.val == 5
