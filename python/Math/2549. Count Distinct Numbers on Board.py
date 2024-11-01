# 2549. Count Distinct Numbers on Board
# https://leetcode.com/problems/count-distinct-numbers-on-board/description/

# Date: Aug 25, 2024
# Difficulty: Easy

# Solution
class Solution(object):
    def distinctIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        return n - 1


# Test case
solution = Solution()

n = 5
result = solution.distinctIntegers(n)
print(result) # 4