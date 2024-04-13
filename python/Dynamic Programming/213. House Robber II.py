# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/description/

# Date: Apr 12, 2024
# Difficulty: Medium

# Solution
import collections
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 3:
            return max(nums)

        # change this problem into House robber I
        def rob_noncircle(nums):
            if len(nums) <= 2:
                return max(nums)

            dp = collections.OrderedDict()
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

            return dp.popitem()[1] # key:0, value:1

        return max(rob_noncircle(nums[1:]), rob_noncircle(nums[:-1]))

# Test case
solution = Solution()

nums = [1,2,3,1]
result = solution.rob(nums)
print(result) # 4