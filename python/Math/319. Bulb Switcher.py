# 319. Bulb Switcher
# https://leetcode.com/problems/bulb-switcher/description/

# Date: Aug 25, 2024
# Difficulty: Medium

from math import floor, sqrt
# Solution
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(floor(sqrt(n)))


# Test case
solution = Solution()

n = 3
result = solution.bulbSwitch(n)
print(result) # 1