# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/

# Date: March 25, 2024
# Difficulty: Medium

# Solution: 
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # initiate dp, with the last column and row set to 1
        dp = [[0 for _ in range(n - 1)] + [1] for _ in range(m)]
        dp[-1] = [1 for _ in range(n)]

        # recursively add up the number of possible routes
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]

# Test case
solution = Solution()

m = 3; n = 7
result = solution.uniquePaths(m, n)

print(result) # 28
