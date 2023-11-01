# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Date: Jul 02, 2023
# Difficulty: Easy

# Time: O(n)
# Space: O(1)

# Solution 1
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k

# Test case
solution = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]
result = solution.removeDuplicates(nums)
print(result)