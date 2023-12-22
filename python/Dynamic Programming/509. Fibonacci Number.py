# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

# Date: Nov 1, 2023
# Difficulty: Easy

# Solution 1: bottom-up (tabulation)
# Time: O(n), Space: O(n)
import collections
class Solution1(object):
    dp = collections.defaultdict(int)
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dp[1] = 1
        for i in range(2, len(n)):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]

        return self.dp[n]

# Solution 2: top-down (memoization)
# Time: O(n), Space: O(n)
class Solution2(object):
    dp = collections.defaultdict(int)
    def fib(self, n):
        if n<=1:
            return n
        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]

# Solution 3: brute-force
# Time: O(2^n), Space: O(n)
class Solution3(object):
    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

# Solution 4: use two variables
# Time: O(n), Space: O(1)
class Solution4(object):
    def fib(self, n):
        previous, current = 0, 1
        if n <= 1:
            return n
        for i in range(n - 1):
            previous, current = current, previous + current

        return current

# Solution 5: matrix
# Time: O(log n), Space: O(1)
import numpy as np
class Solution5(object):
    def fib(self, n):
        M = np.matrix([[0,1],[1,1]])
        vec = np.array([[0],[1]])
        return np.matmul(M**n, vec)[0]

# Test case
solution = Solution2()
n = 4
result = solution.fib(n)
print(result) # 3