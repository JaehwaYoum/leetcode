# 1005. Maximize Sum Of Array After K Negations
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/

# Date: Apr 20, 2024
# Difficulty: Easy

# Solution
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

# Test case
solution = Solution()
nums = [4,2,3]; k = 1		
result = solution.largestSumAfterKNegations(nums, k)
print(result)