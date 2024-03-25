# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

# Date: Feb 25, 2024
# Difficulty: Medium

# The algorithm must run in O(n) time and uses only constant extra space.

# Solution
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = []
        counter = {}

        for i in range(len(nums)):
            if nums[i] in counter:
                result.append(nums[i])
            counter[nums[i]] = 1
        return result


# Test case
solution = Solution()

nums = [4,3,2,7,8,2,3,1]
result = solution.findDuplicates(nums)
print(result)  # 1