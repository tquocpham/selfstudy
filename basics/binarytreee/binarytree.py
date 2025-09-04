from typing import Union, List


class BinaryNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def has_child(node: BinaryNode):
    return node.left is not None or node.right is not None


def insert(headnode: BinaryNode, value):
    if value < headnode.value:
        if headnode.left:
            insert(headnode.left, value)
        else:
            headnode.left = BinaryNode(value)
    if value > headnode.value:
        if headnode.right:
            insert(headnode.right, value)
        else:
            headnode.right = BinaryNode(value)


def printtree(n: BinaryNode):
    if n.left:
        printtree(n.left)
    print(n.value)
    if n.right:
        printtree(n.right)


def inorder_traversal_iterative(headnode: BinaryNode):
    result = []
    stack = []
    current: BinaryNode = headnode

    while current or stack:
        # Traverse left subtree and push nodes onto the stack

        while current:
            stack.append(current)
            current = current.left

        # Pop a node, process it, and move to its right child
        print([n.value for n in stack])
        current = stack.pop()
        result.append(current.value)
        current = current.right

    return result
