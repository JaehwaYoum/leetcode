# 703. Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

# Date: Jul 6, 2024
# Difficulty: Easy

# Solution
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k  = k
        self.nums = nums

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k-1]


# Test case
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))  # return 4
print(kthLargest.add(5))   # return 5
print(kthLargest.add(10))  # return 5
print(kthLargest.add(9))    # return 8
print(kthLargest.add(4))    # return 8