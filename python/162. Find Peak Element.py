# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/

# Date: Jul 12, 2023
# Difficulty: Medium

# Time: O(n)
# Space: O(1)

# Solution 1
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = nums[0]
        index = 0

        for i in range(1,len(nums)):
            if nums[i] > max:
                max = nums[i] # update max
                index = i

        return index

# Test case
solution = Solution()

nums = [1,2,1,3,5,6,4]
result = solution.findPeakElement(nums)
print(result)
# 5