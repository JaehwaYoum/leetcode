# 740. Delete and Earn
# https://leetcode.com/problems/delete-and-earn/description/

# Date: Feb 25, 2024
# Difficulty: Medium

# Solution: Dynamic Programming
import collections
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        # convert the nums into a frequency list
        # [3, 4, 2] -> [0, 0, 2, 3, 4]
        # [2, 2, 3, 3, 3, 4] -> [0, 0, 4, 9, 6]
        freq = [0] * (max(nums) + 1)
        for num in nums:
            freq[num] += num

        # now this is a house robber problem
        # https://leetcode.com/problems/house-robber/
        if len(freq) <=2:
            return max(freq[0], freq[1])

        dp = collections.OrderedDict()
        dp[0], dp[1] = freq[0], max(freq[0], freq[1])

        for i in range(2, len(freq)):
            dp[i] = max(dp[i-1], dp[i-2]+freq[i])

        return dp.popitem()[1]


# Test case
solution = Solution()
nums = [2,2,3,3,3,4]
result = solution.deleteAndEarn(nums)
print(result) # 9

