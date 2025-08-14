from typing import Union


class BinaryNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class LLNode:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value


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


def printll(n: LLNode):
    print(n.value)
    if n.next:
        printll(n.next)


arr = [5, 6, 4, 7, 9, 10, 11, 15, 7, 45, 24, 5, 67]
headnode = BinaryNode(12)
for a in arr:
    # print(a)
    insert(headnode, a)
# printtree(headnode)
tracker = LLTracker()
to_dbl_linked_list(headnode, tracker)
print(tracker.ptr.value)

curr = tracker.ptr
while True:
    print(curr.value)
    if curr.next:
        curr = curr.next
    else:
        break

while True:
    print(curr.value)
    if curr.prev:
        curr = curr.prev
    else:
        break
