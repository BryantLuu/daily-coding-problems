"""

Good morning. Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """

 """
 My approach:
    First, check if the current node would part of the above nodes unival tree. If we are the last node, return 1 and the boolean.
    If we are not the last node, return the unival count from the left and right subtrees and whether below nodes are unival trees
 """

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def count_unival_subtrees(node):
    def count_subtrees(node, value):
        is_unival = node.value == value
        if not node.left and node.right:
            return 1, is_unival
        left_count = right_count = 0
        is_left_unival = is_right_unival = True
        if node.left:
            left_count, is_left_unival = count_subtrees(node.left, node.value)
        if node.right:
            right_count, is_right_unival = count_subtrees(node.right, node.value)
        count = left_count + right_count
        if is_left_unival and is_right_unival:
            count += 1
        return count, is_left_unival and is_right_unival and is_unival
    left_count, is_left_unival = count_subtrees(node.left, node.value)
    right_count, is_right_unival = count_subtrees(node.right, node.value)
    count = left_count + right_count
    if is_left_unival and is_right_unival:
        return count + 1
    return count

node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
assert count_unival_subtrees(node) == 5
