from binarytree import BinaryNode


class LLNode:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value


class LLTracker:
    def __init__(self):
        self.ptr: LLNode = None


def to_dbl_linked_list(n: BinaryNode, tracker: LLTracker):
    if n.right:
        to_dbl_linked_list(n.right, tracker)

    node = LLNode(n.value)
    if tracker.ptr is None:
        tracker.ptr = node
    else:
        tracker.ptr.prev = node
        node.next = tracker.ptr
        tracker.ptr = node

    if n.left:
        to_dbl_linked_list(n.left, tracker)


def ll_print(n: LLNode):
    print(n.value)
    if n.next:
        ll_print(n.next)
