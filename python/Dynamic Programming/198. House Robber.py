# 198. House Robber
# https://leetcode.com/problems/house-robber/

# Date: Dec 27, 2023
# Difficulty: Medium

# Solution: Dynamic Programming
import collections
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 2:
            return max(nums)

        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp.popitem()[1]

# Test case
solution = Solution()
nums = [2,7,9,3,1]
result = solution.rob(nums)
print(result) # 12

