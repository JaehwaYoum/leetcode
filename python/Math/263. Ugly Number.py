# 263. Ugly Number
# https://leetcode.com/problems/ugly-number/

# Date: Jan 24, 2025
# Difficulty: Easy

# Solution: recursive
class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        for p in [2, 3, 5]:
            while n % p == 0:
                n /= p
        
        return n == 1


# Test case
solution = Solution()

n = 14
result = solution.isUgly(x, n)

print(result) # False
