# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/

# Date: Sep 24, 2023
# Difficulty: Easy

# Time: O(n), Space: O(1)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        k = 0
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
            else:
                zero_count += 1

        for j in range(-1, -zero_count - 1, -1):
            nums[j] = 0

# Test case : in-place without making a copy of the array.
solution = Solution()

nums = [0,1,0,3,12]
solution.moveZeroes(nums)
print(nums) # [1, 3, 12, 0, 0]