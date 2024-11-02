# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/

# Date: Nov 22, 2023 | Nov 1, 2024
# Difficulty: Easy

# Solution 1
# Time: O(log n), Space: O(1)
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
# Time: O(log n), Space: O(log n)
class Solution2(object):
    def hammingWeight(self, n):
        return bin(n).count('1')

# Solution 3
# Time: O(log n), Space: O(log n)
class Solution3(object):
    def hammingWeight(self, n):

        if n==0:
            return 0
        return n%2 + self.hammingWeight(n//2)


# Test case
solution = Solution3()
n = 2147483645
result = solution.hammingWeight(n)
print(result) # 30
