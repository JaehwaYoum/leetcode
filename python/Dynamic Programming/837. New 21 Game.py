# 837. New 21 Game
# https://leetcode.com/problems/new-21-game/description/

# Date: Aug 17, 2024
# Difficulty: Medium

# Solution
# Time: O(n), Space: O(n)
class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        
        if k == 0 or n - k >= maxPts:
            return 1

        dp = [1.0] + [0.0] * n  # declare an array of float
        cumProb = 1.0

        for i in range(1, n+1):
            dp[i] = cumProb / maxPts
            if i < k:
                cumProb += dp[i]
            if i >= maxPts:
                cumProb -= dp[i - maxPts]

        return sum(dp[k:])

# Test case
solution = Solution()

n = 21; k = 17; maxPts = 10
result = solution.new21Game(n, k, maxPts)
print(result) 
