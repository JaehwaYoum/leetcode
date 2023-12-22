# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/

# Date: Nov 2, 2023
# Difficulty: Medium

# Solution
# Time: O(n), Space: O(1)
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        red, white, blue = 0, 0, len(nums)

        while white < blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 2:
                blue -= 1
                nums[blue], nums[white] = nums[white], nums[blue]
            else:
                white += 1

        return nums

# Test case
solution = Solution()
nums = [2,0,2,1,1,0]
result = solution.sortColors(nums)
print(result) # [0, 0, 1, 1, 2, 2]