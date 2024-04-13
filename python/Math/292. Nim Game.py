# 292. Nim Game
# https://leetcode.com/problems/nim-game/description/

# Date: Apr 12, 2024
# Difficulty: Easy

# Solution
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n % 4 == 0:
            return False
        else:
            return True



# Test case
solution = Solution()

n = 4
result = solution.canWinNim(n)
print(result)