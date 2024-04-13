# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/description/

# Date: Apr 12, 2024
# Difficulty: Medium

# Solution
import collections
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        # initialize the first row 
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # initialize the first column 
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # fill the rest 
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]

# Test case
solution = Solution()

grid = [[1,3,1],[1,5,1],[4,2,1]]
result = solution.minPathSum(grid)
print(result) # 7