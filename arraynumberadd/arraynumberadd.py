#  Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        max_len = max(len(l1), len(l2))
        answer = []
        carry = 0
        i = 0
        for i in range(max_len):
            if i < len(l1):
                v1 = l1[i]
            else:
                v1 = 0
            if i < len(l2):
                v2 = l2[i]
            else:
                v2 = 0
            total = v1 + v2 + carry
            carry = int(total/10)
            value = total % 10
            answer.append(value)
        if carry:
            answer.append(carry)
        return answer


sln = Solution()
print(sln.addTwoNumbers([2, 4, 3], [5, 6, 4]))
print(sln.addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
