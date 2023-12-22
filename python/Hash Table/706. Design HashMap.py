# 706. Design HashMap
# https://leetcode.com/problems/design-hashmap/

# Date: Dec 18, 2023
# Difficulty: Easy

class ListNode():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

import collections
class MyHashMap(object):

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.size

        # if no node at the index
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # hash collision
        p = self.table[index]
        while p:
            # checks if the key exists, update the value
            if p.key == key:
                p.value = value
                return
            # if the key does not exist, break the loop
            if p.next is None:
                break
            p = p.next
        # appends a new ListNode to the end of the linked list
        p.next = ListNode(key, value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # calculates the index where the key should be located
        index = key % self.size

        # the key is not present, returns -1
        if self.table[index].value is None:
            return -1

        # looks for the matching key
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % self.size

        # the key is not present, does nothing
        if self.table[index].value is None:
            return

        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        prev = p # prev used to keep track of the previous node
        while p:
            if p.key == key:
                prev.next = p.next # disconnects the current node p by bypassing it
                return
            prev, p = p, p.next # traverse linked lists

# Test case
myHashMap = MyHashMap()

myHashMap.put(1, 1)
myHashMap.put(2, 2)

result1 = myHashMap.get(1)
print(f"get(1) => {result1}")

result3 = myHashMap.get(3)
print(f"get(3) => {result3}")

myHashMap.put(2, 1)

result2 = myHashMap.get(2)
print(f"get(2) => {result2}")

myHashMap.remove(2)
result2_removed = myHashMap.get(2)
print(f"get(2) after remove => {result2_removed}")