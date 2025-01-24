# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/description/

# Date: Oct 31, 2024
# Difficulty: Medium

# Time: O(1), Space: O(capacity)
import collections
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = abs(capacity)
        self.cache = collections.OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)



# Test case : in-place without making a copy of the array.
cache = LRUCache(2)

# Test case 1
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Expected output: 1

# Test case 2 - Adding third item, which should evict key 2 as capacity is 2
cache.put(3, 3)
print(cache.get(2))  # Expected output: -1 (not found)

# Test case 3 - Adding fourth item, which should evict key 1
cache.put(4, 4)
print(cache.get(1))  # Expected output: -1 (not found)
print(cache.get(3))  # Expected output: 3
print(cache.get(4))  # Expected output: 4
