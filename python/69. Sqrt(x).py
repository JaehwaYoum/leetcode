# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/

# Date: Sep 30, 2023
# Difficulty: Easy

# Time: O(log x), Space: O(1)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x <= 1:
            return x

        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                right = mid
            else:
                left = mid
# Test case
solution = Solution()

x = 100
result = solution.mySqrt(x)
print(result)
