# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

# Date: Jul 12, 2023
# Difficulty: Medium

# Time: O(n)
# Space: O(1)

# Solution 1
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        currentsum = 0
        maxsum = float('-inf')
        startindex = 0
        endindex = -1

        # Update current sum by adding the current element
        for i in range(len(nums)):
            if currentsum < 0:
                currentsum = nums[i]
                startindex = i
            else:
                currentsum += nums[i]

            # Check if the current sum is greater than the maximum sum
            if currentsum > maxsum:
                maxsum = currentsum
                endindex = i

        return maxsum

# Test case
solution = Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
result = solution.maxSubArray(nums)
print(result)
# 6
# The subarray [4,-1,2,1] has the largest sum 6.