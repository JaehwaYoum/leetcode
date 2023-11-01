# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# Date: Jul 02, 2023
# Difficulty: Medium

# Time: O(n)
# Space: O(1)

# Solution 1
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k = 0

        for n in nums:
            if k < 2 or n > nums[k - 2]:
                nums[k] = n
                k += 1

        return k

# Test case
solution = Solution()

nums = [0,0,1,1,1,1,2,3,3]
result = solution.removeDuplicates(nums)
print(result)