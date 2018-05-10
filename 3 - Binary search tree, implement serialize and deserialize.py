"""
Good morning. Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
Upgrade to premium and get in-depth solutions to every problem.

If you liked this problem, feel free to forward it along! As always, shoot us an email if there's anything we can help with!
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    vals = []
    nodes = []
    def get_values(node):
        if node.left:
            vals.append(node.left.val)
            nodes.append(node.left)
        else:
            vals.append(str(None))
        if node.right:
            vals.append(node.right.val)
            nodes.append(node.right)
        else:
            vals.append(str(None))
    vals.append(node.val)
    get_values(node)
    while nodes:
        get_values(nodes.pop(0))
    return ','.join(vals)

def deserialize(s):
    nodes = s.split(',')
    saved_nodes = []
    root =  Node(nodes.pop(0))
    def add_nodes(node):
        if nodes:
            node_value = nodes.pop(0)
            if node_value:
                new_node = Node(node_value)
                node.left = new_node
                saved_nodes.append(new_node)
            else:
                node.left = node_value
        if nodes:
            node_value = nodes.pop(0)
            if node_value:
                new_node = Node(node_value)
                node.right = new_node
                saved_nodes.append(new_node)
            else:
                node.right = node_value
    add_nodes(root)
    while saved_nodes:
        if saved_nodes:
            add_nodes(saved_nodes.pop(0))
        if saved_nodes:
            add_nodes(saved_nodes.pop(0))
    return root
    
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
