# 2210. Count Hills and Valleys in an Array
# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

# Date: Mar 30, 2024
# Difficulty: Easy

# Solution
# Time: O(n), Space: O(1)
class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0

        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                # if the adjacent numbers are equal, update the current value to the previous one
                nums[i] = nums[i - 1]

            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]: # hill check
                result += 1
            elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]: # valley check
                result += 1

        return result


# Test case
solution = Solution()

nums = [2,4,1,1,6,5]
result = solution.countHillValley(nums)

print(result) # 3