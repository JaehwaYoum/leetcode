# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/

# Date: Nov 1, 2023
# Difficulty: Easy

# Solution
class MyQueue(object):

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.output.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return self.input == [] and self.output == []

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
print(param_2)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)