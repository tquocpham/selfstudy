# 895. Maximum Frequency Stack
# Hard
# Topics
# premium lock icon
# Companies
# Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

# Implement the FreqStack class:

# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the stack.
# If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.


# Example 1:

# Input
# ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
# [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
# Output
# [null, null, null, null, null, null, null, 5, 7, 5, 4]

# Explanation
# FreqStack freqStack = new FreqStack();
# freqStack.push(5); // The stack is [5]
# freqStack.push(7); // The stack is [5,7]
# freqStack.push(5); // The stack is [5,7,5]
# freqStack.push(7); // The stack is [5,7,5,7]
# freqStack.push(4); // The stack is [5,7,5,7,4]
# freqStack.push(5); // The stack is [5,7,5,7,4,5]
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
# freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
# freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].


# Constraints:

# 0 <= val <= 109
# At most 2 * 104 calls will be made to push and pop.
# It is guaranteed that there will be at least one element in the stack before calling pop.


class FreqStack:

    def __init__(self):
        self.__stack = []
        self.__counter = {}

    def push(self, val: int) -> None:
        if val not in self.__counter:
            self.__counter[val] = 0
        self.__counter[val] += 1
        self.__stack.insert(0, val)

    def pop(self) -> int:
        most_freq = []
        max_count = 0
        for v, c in self.__counter.items():
            if c > max_count:
                most_freq = [v]
                max_count = c
            if c == max_count:
                most_freq.append(v)
        return self.__pop_recent(most_freq)

    def __pop_recent(self, values):
        print(self.__counter, self.__stack)
        for i in range(len(self.__stack)):
            v = self.__stack[i]
            if v in values:
                self.__counter[v] -= 1
                return self.__stack.pop(i)
        raise Exception('no more stuff to Pop! Pop!')


# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
