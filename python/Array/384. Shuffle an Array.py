# 384. Shuffle an Array
# https://leetcode.com/problems/shuffle-an-array/

# Date: Nov 1, 2024
# Difficulty: Medium

import random
# Solution
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums[:]
        self.orig_nums = nums[:]

    def reset(self):
        return self.orig_nums

    def shuffle(self):
        random.shuffle(self.nums)
        return self.nums

# Test case
nums = [1, 2, 3, 4, 5, 6]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
param_3 = obj.reset()

print(obj)
print(param_1) # orginal
print(param_2) # shuffled
print(param_3) # original