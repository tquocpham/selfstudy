from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}'


def printll(ll):
    c = ll
    str = ''
    while c:
        str += f'{c.val},'
        c = c.next
    print(str)


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        currNode = head
        prevNode = None
        count = 1
        tailingNode = None
        firstNode = None
        newHead = head
        while currNode:
            print(currNode)
            if count < left:
                tailingNode = currNode
                firstNode = currNode.next
                print(tailingNode, firstNode)
                currNode = currNode.next
                count += 1
                continue
            if count > right:
                if firstNode:
                    firstNode.next = currNode
                    firstNode = None
                currNode = currNode.next
                count += 1
                continue

            tailingNode.next = currNode
            placeholder = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = placeholder
            count += 1

        return newHead


def convert(lst):
    lst.reverse()
    last = None
    for n in lst:
        last = ListNode(n, last)
    return last


sln = Solution()
ll = convert([1, 2, 3, 4, 5, 6, 7, 8])
ll = sln.reverseBetween(ll, 2, 4)
printll(ll)


# Output: [1,4,3,2,5]
