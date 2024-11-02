# 155. Min Stack
# https://leetcode.com/problems/min-stack/

# Date: Nov 1, 2024
# Difficulty: Medium

import random
# Solution
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            popped = self.stack.pop()
            if popped == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None



# Test case
obj = MinStack()
vals = [-2, 0, -3]
for val in vals:
    obj.push(val)
param_1 = obj.getMin()
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

print(obj)
print(param_1) # return -3
print(param_2)
print(param_3) # return 0
print(param_4) # return -2