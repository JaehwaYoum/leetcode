# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/description/

# Date: Jan 27, 2024
# Difficulty: Easy

# Solution 1
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left_sum = 0
        right_sum = sum(nums[1:])

        # return the first index when the right sum is 0
        if right_sum == 0:
            return 0

        # move the pivot and return the leftmost pivot index
        for i in range(1, len(nums)):
            left_sum += nums[i - 1]
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i

        # return -1 when no such index exists
        return -1

# Test case
solution = Solution()

nums = [1,7,3,6,5,6]
result = solution.pivotIndex(nums)
print(result) # 3