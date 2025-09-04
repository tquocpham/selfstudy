from binarytree import BinaryNode, has_child


def min_heapify(headnode: BinaryNode):
    bfs_queue = [headnode]
    to_sift = [headnode]
    while len(bfs_queue):
        node = bfs_queue.pop(0)
        if node.left:
            bfs_queue.append(node.left)
            if has_child(node.left):
                to_sift.insert(0, node.left)
        if node.right:
            bfs_queue.append(node.right)
            if has_child(node.right):
                to_sift.insert(0, node.right)

    for node in to_sift:
        values = [node.value]
        if node.left:
            values.append(node.left.value)
        if node.right:
            values.append(node.right.value)
        min_value = min(values)
        if min_value == node.value:
            # nothing to do good here.
            continue
        elif node.left and min_value == node.left.value:
            swap_left(node)
        elif node.right and min_value == node.right.value:
            swap_right(node)


def swap_left(node: BinaryNode):
    pl = node.value
    node.value = node.left.value
    node.left.value = pl


def swap_right(node: BinaryNode):
    pl = node.value
    node.value = node.right.value
    node.left.value = pl
