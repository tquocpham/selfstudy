# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        currNode = head
        stack = []
        while currNode:
            stack.insert(0, currNode.val)
            currNode = currNode.next
        currNode = head
        while currNode:
            v = stack.pop(0)
            if currNode.val != v:
                return False
            currNode = currNode.next
        return True


def convert(string):
    ll = None
    for c in string[::-1]:
        ll = ListNode(c, ll)
    return ll


sln = Solution()
print(sln.isPalindrome(convert('racecar')))
print(sln.isPalindrome(convert('asdfasfd')))
