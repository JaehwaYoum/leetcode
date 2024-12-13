# 1413. Minimum Value to Get Positive Step by Step Sum
# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

# Date: Nov 10, 2024
# Difficulty: Easy


# Solution
# Time: O(n), Space: O(n)
class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = dp[i-1] + nums[i]
        
        min_val = min(dp)
        return - min_val + 1 if min_val < 0 else 1
        


# Test case
solution = Solution()

nums = [-3,2,-3,4,2]
result = solution.minStartValue(nums)

print(result) # 5
