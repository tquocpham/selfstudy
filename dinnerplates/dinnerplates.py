# 1172. Dinner Plate Stacks
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.

# Implement the DinnerPlates class:

# DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks capacity.
# void push(int val) Pushes the given integer val into the leftmost stack with a size less than capacity.
# int pop() Returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all the stacks are empty.
# int popAtStack(int index) Returns the value at the top of the stack with the given index index and removes it from that stack or returns -1 if the stack with that given index is empty.


# Example 1:

# Input
# ["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"]
# [[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]
# Output
# [null, null, null, null, null, null, 2, null, null, 20, 21, 5, 4, 3, 1, -1]

# Explanation:
# DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
# D.push(1);
# D.push(2);
# D.push(3);
# D.push(4);
# D.push(5);         // The stacks are now:  2  4
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 2.  The stacks are now:     4
#                                                        1  3  5
#                                                        ﹈ ﹈ ﹈
# D.push(20);        // The stacks are now: 20  4
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.push(21);        // The stacks are now: 20  4 21
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
#                                                         1  3  5
#                                                         ﹈ ﹈ ﹈
# D.popAtStack(2);   // Returns 21.  The stacks are now:     4
#                                                         1  3  5
#                                                         ﹈ ﹈ ﹈
# D.pop()            // Returns 5.  The stacks are now:      4
#                                                         1  3
#                                                         ﹈ ﹈
# D.pop()            // Returns 4.  The stacks are now:   1  3
#                                                         ﹈ ﹈
# D.pop()            // Returns 3.  The stacks are now:   1
#                                                         ﹈
# D.pop()            // Returns 1.  There are no stacks.
# D.pop()            // Returns -1.  There are still no stacks.


# Constraints:

# 1 <= capacity <= 2 * 104
# 1 <= val <= 2 * 104
# 0 <= index <= 105
# At most 2 * 105 calls will be made to push, pop, and popAtStack.

class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.__matrix = [[]]
        self.__capacity = capacity

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        for i in range(len(self.__matrix)):
            row = self.__matrix[i]
            if len(row) < self.__capacity:
                row.insert(0, val)
                print(self.__matrix)
                return

        self.__matrix.append([val])

        # row = self.__matrix[self.__least_filled_ptr]
        # while len(row) == self.__capacity:
        #     self.__least_filled_ptr += 1
        #     if len(self.__matrix)-1 < self.__least_filled_ptr:
        #         self.__c += 1
        #         self.__matrix.append([])
        #     row = self.__matrix[self.__least_filled_ptr]
        # row.append(val)

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.__matrix)-1, 0, -1):
            row = self.__matrix[i]
            if len(row) > 0:
                print(self.__matrix)
                return row.pop(0)

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index > len(self.__matrix):
            return -1
        if len(self.__matrix[index]) == 0:
            return -1
        return self.__matrix[index].pop(0)


dp = DinnerPlates(2)
dp.push(1)
dp.push(2)
dp.push(3)
dp.push(4)
dp.push(5)
dp.push(6)
dp.push(7)
dp.push(8)
dp.push(8)
dp.push(8)
dp.push(9)
dp.push(8)
dp.push(9)
dp.push(8)
dp.push(9)
print(dp.pop())
print(dp.pop())
print(dp.pop())
print(dp.pop())
print(dp.pop())
print(dp.pop())
print(dp.pop())
print(dp.pop())
print(dp.popAtStack(0))
print(dp.popAtStack(0))
print(dp.popAtStack(0))

print(dp.popAtStack(1))
print(dp.popAtStack(1))
print(dp.popAtStack(1))

dp.push(8)
dp.push(9)
dp.push(8)

print(dp.popAtStack(0))
print(dp.popAtStack(0))
print(dp.popAtStack(0))

print(dp.popAtStack(1))
print(dp.popAtStack(1))
print(dp.popAtStack(1))
