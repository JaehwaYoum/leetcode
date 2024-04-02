# 1218. Longest Arithmetic Subsequence of Given Difference
# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

# Date: Mar 30, 2024
# Difficulty: Medium

import collections
# Solution
class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """

        dp = collections.defaultdict(int)

        for num in arr:
            # look  up the length of the longest subsequence ending with
            # (num - difference) and add 1 to it
            dp[num] = dp[num - difference] + 1

        return max(dp.values())


# Test case
solution = Solution()

arr = [1,5,7,8,5,3,4,2,1]; difference = -2
result = solution.longestSubsequence(arr, difference)

print(result) # 0.0625
