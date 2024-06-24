
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_to_list(root: TreeNode) -> list:
    result = []

    def inorder_traversal(node):
        if node:
            result.append(node.val)
            inorder_traversal(node.left)
            inorder_traversal(node.right)

    inorder_traversal(root)
    return result

def list_to_tree(nodes:list) -> TreeNode:
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    i = 1 # start from the second element of the list
    queue = [root]

    while queue:
        node = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root


# Print Tree
import collections
def printTree(root: TreeNode) -> None:
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
