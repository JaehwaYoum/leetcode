
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_to_list(root):
    result = []

    def inorder_traversal(node):
        if node:
            result.append(node.val)
            inorder_traversal(node.left)
            inorder_traversal(node.right)

    inorder_traversal(root)
    return result


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
