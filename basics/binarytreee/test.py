from binarytree import BinaryNode, printtree, insert
from heap import min_heapify
from linked_list import LLTracker, to_dbl_linked_list


def test_min_heapify():
    print(f'testing_min_heapify')
    arr = [5, 6, 4, 7, 9, 10, 11, 15, 7, 45, 24, 67]
    headnode = BinaryNode(12)

    for a in arr:
        # print(a)
        insert(headnode, a)
    min_heapify(headnode)
    assert 4 == headnode.value


test_min_heapify()


arr = [5, 6, 4, 7, 9, 10, 11, 15, 7, 45, 24, 67]
headnode = BinaryNode(12)

for a in arr:
    # print(a)
    insert(headnode, a)

# print(inorder_traversal_iterative(headnode))


# printtree(headnode)
tracker = LLTracker()
to_dbl_linked_list(headnode, tracker)
print(f"tracker.ptr.value {tracker.ptr.value}")

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
