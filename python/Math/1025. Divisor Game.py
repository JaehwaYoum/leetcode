# 1025. Divisor Game
# https://leetcode.com/problems/divisor-game/

# Date: Mar 30, 2024
# Difficulty: Easy

# Solution
# Anyone who gets 1 definitely loses.
# Anyone who gets 2 definitely wins since he always/or only can make 2 become 1.
# For any n >= 2, N will definitely be reduced to 2.

class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n % 2 == 0:
            return True
        else:
            return False
