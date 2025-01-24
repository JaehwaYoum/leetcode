# 896. Monotonic Array
# https://leetcode.com/problems/monotonic-array/

# Date: Jan 24, 2025
# Difficulty: Easy

# Solution 1: Iterative 
# Time: O(n), Space: O(1)
class Solution1(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True

        decreasing, increasing = True, True
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                decreasing = False
            elif nums[i] > nums[i-1]:
                increasing = False

        return increasing or decreasing


# Solution 2
# Time: O(n log n), Space: O(n)
class Solution2(object):
    def isMonotonic(self, nums): 
        if nums == sorted(nums): # sorted method creates a new array (uses merge sort)
            return True
        elif nums == sorted(nums, reverse=True):
            return True
        else:
            return False



# Test case
solution = Solution2()

nums = [6,5,4,4]
result = solution.isMonotonic(nums)
print(result) # True