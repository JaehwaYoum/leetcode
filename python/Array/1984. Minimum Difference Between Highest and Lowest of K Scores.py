# 1984. Minimum Difference Between Highest and Lowest of K Scores
# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

# Date: Mar 30, 2024
# Difficulty: Easy

# Solution
class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if len(nums) == 1:
            return 0

        nums = sorted(nums)
        result = nums[k-1] - nums[0]

        for i in range(k, len(nums)):
            result = min(result, nums[i] - nums[i - k + 1])

        return result


# Test case
solution = Solution()

nums = [9,4,1,7]; k = 2
result = solution.minimumDifference(nums, k)

print(result) # 2
