# Definition for a n-ary tree node.
from collections import deque

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def tree_to_list(root: Node) -> list:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        for child in node.children:
            queue.append(child)

        # Add None to indicate the end of children for this node
        if not node.children:
            result.append(None)

    return result

def list_to_tree(nodes: list) -> Node:
    if not nodes or nodes[0] is None:
        return None

    root = Node(nodes[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):
        node = queue.popleft()
        children = []

        # Process all children until we encounter a None marker
        while i < len(nodes) and nodes[i] is not None:
            child = Node(nodes[i])
            children.append(child)
            queue.append(child)
            i += 1

        # Move past the None marker if it's there
        if i < len(nodes) and nodes[i] is None:
            i += 1

        # Assign collected children to the current node
        node.children = children

    return root



# Example usage
# Create the tree
root = Node(1, [
    Node(2),
    Node(3),
    Node(4, [
        Node(5),
        Node(6)
    ])
])

# Convert the tree to a list
tree_list = tree_to_list(root)
print(tree_list)  # Expected output: [1, 2, None, 3, None, 4, 5, None, 6, None]

# Convert the list back to a tree
restored_root = list_to_tree(tree_list)

# Verify the restored tree
restored_list = tree_to_list(restored_root)
print(restored_list)  # Expected output: [1, 2, None, 3, None, 4, 5, None, 6, None]