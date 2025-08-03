
# 25. Reverse Nodes in k-Group
# Hard
# Topics
# premium lock icon
# Companies
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.


# Example 1
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Example 2
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]


from typing import Union, Optional, List
# Definition for singly-linked list.


def printll(ll):
    c = ll
    while c:
        print(c)
        c = c.next


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __str__(self):
        return f'<{str(self.val)}.{id(self)}>'


def convert(array: List[int]) -> ListNode:
    last = None
    array.reverse()
    for a in array:
        last = ListNode(a, last)
    return last


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        currNode = head
        counter = 0
        lastEndNode = None
        firstNode = None
        newHead = None
        while currNode is not None:
            if 0 == counter % k:
                firstNode = currNode
            if k-1 == counter:
                newHead = currNode
            if (k-1) == counter % k:
                prevNode = currNode.next
                cNode = firstNode
                while True:
                    placeholder = cNode.next
                    cNode.next = prevNode

                    if cNode is currNode:
                        currNode = firstNode
                        if lastEndNode:
                            lastEndNode.next = cNode
                        break
                    prevNode = cNode
                    cNode = placeholder

                lastEndNode = currNode

            counter += 1
            currNode = currNode.next
        return newHead


ll = convert([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
             12, 13, 14, 15, 16, 17, 18, 19])
sln = Solution()
ll = sln.reverseKGroup(ll, 5)
print('out')
printll(ll)
