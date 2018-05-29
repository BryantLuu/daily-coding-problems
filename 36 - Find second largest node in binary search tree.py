class Node:
    left = None
    right = None
    def __init__(self, value):
        self.value = value

def find_second_largest_node(root):
    largest_node = root
    second_largest_node = None
    def traverse(node):
        nonlocal largest_node
        nonlocal second_largest_node
        if not node:
            return
        if node.value > largest_node.value:
            second_largest_node = largest_node
            largest_node = node
        if not second_largest_node or node.value > second_largest_node.value:
            second_largest_node = node
        traverse(node.left)
        traverse(node.right)
    traverse(root.left)
    traverse(root.right)
    return largest_node.value, second_largest_node.value

node = Node(3)
node.left = Node(2)
node.right = Node(1)
print(find_second_largest_node(node))
