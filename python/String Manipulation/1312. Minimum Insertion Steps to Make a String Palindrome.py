# 1312. Minimum Insertion Steps to Make a String Palindrome
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/

# Date: Nov 5, 2023
# Difficulty: Hard

# Solution: bottom-up dynamic programming
# Time: O(n^2), Space: O(n^2)
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        dp = [[0] * n for _ in range(n)]


        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

        return dp[0][n - 1]

# Test case
solution = Solution()

s = "leetcode"
result = solution.minInsertions(s)
print(result) # 5