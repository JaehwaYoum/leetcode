# 896. Monotonic Array
# https://leetcode.com/problems/monotonic-array/description/

# Date: Feb 9, 2024
# Difficulty: Easy

# Solution
class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == sorted(nums):
            return True
        elif nums == sorted(nums, reverse=True):
            return True
        else:
            return False

# Test case
solution = Solution()

nums = [1,2,2,3]
result = solution.isMonotonic(nums)
print(result) # True
