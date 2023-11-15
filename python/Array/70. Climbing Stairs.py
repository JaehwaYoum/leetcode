# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

# Date: Nov 15, 2023
# Difficulty: Easy

# Fibonacci that start at f(1)=1, f(2)=2
class Solution1(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        previous = 0
        current = 1

        for i in range(n):
                previous, current = current, previous + current

        return current

# top-down (memoization)
import collections
class Solution2(object):
    dp = collections.defaultdict(int)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]

# Test case
solution = Solution1()
n = 3
result = solution.climbStairs(n)
print(result) # 3