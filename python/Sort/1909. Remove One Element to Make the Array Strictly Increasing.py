# 1909. Remove One Element to Make the Array Strictly Increasing
# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/description/

# Date: Feb 25, 2024
# Difficulty: Easy

class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        removed = False

        for i in range(1, len(nums)):

            # condition to decide whether to remove an element
            if nums[i - 1] >= nums[i]:

                # if more than 1 removal is needed
                if removed:
                    return False
                removed = True

                # check if the array is strictly increasing after removing i-1
                if i == 1 or nums[i - 2] < nums[i]:
                    continue

                # check if the array is strictly increasing after removing i
                elif i < len(nums) - 1 and nums[i - 1] >= nums[i + 1]:
                    return False

        return True

# Test case
solution = Solution()

nums = [1,2,10,5,7]
result = solution.canBeIncreasing(nums)
print(result) # True
