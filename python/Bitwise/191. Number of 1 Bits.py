# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/

# Date: Nov 22, 2023
# Difficulty: Easy

# Solution 1
# Time: O(), Space: O()
class Solution1(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

# Solution 2
# Time: O(), Space: O()
class Solution2(object):
    def hammingWeight(self, n):
        return bin(n).count('1')


# Test case
solution = Solution1()
n = 1101
result = solution.hammingWeight(n)
print(result)
