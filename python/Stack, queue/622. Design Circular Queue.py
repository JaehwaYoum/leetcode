# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/

# Date: Dec 13, 2023
# Difficulty: Medium

class MyCircularQueue(object):
    def __init__(self, k):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value):
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self):
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self):
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self):
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self):
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None


# Test case
circularQueue = MyCircularQueue(3)

# Apply the operations as per the test case
results = [
    None,
    circularQueue.enQueue(1),
    circularQueue.enQueue(2),
    circularQueue.enQueue(3),
    circularQueue.enQueue(4),
    circularQueue.Rear(),
    circularQueue.isFull(),
    circularQueue.deQueue(),
    circularQueue.enQueue(4),
    circularQueue.Rear()
]

print(results) # [null, true, true, true, false, 3, true, true, true, 4]