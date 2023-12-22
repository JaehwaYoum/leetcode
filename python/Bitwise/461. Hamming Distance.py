# 461. Hamming Distance
# https://leetcode.com/problems/hamming-distance/

# Date: Nov 22, 2023
# Difficulty: Easy

# Solution
# Time: O(n), Space: O(1)
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')


# Test case
solution = Solution()
x = 1
y = 4
result = solution.hammingDistance(x, y)
print(result) # 2