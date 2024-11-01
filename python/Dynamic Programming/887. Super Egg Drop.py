# 887. Super Egg Drop
# https://leetcode.com/problems/super-egg-drop/description/

# Date: Aug 25, 2024
# Difficulty: Hard

# Solution 1
# Time: O(k * log n), Space: O(k * log n)
class Solution1(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """

        dp = [[0] * (k+1) for _ in range(n+1)]
        # dp[m][e]: max # of floors that can be checked with m moves and e eggs

        # build the solution incrementally
        for m in range(1, n+1):
            for e in range(1, k+1):
                dp[m][e] = dp[m-1][e-1] + dp[m-1][e] + 1
                # the egg breaks (add max # floors that we can check below the current floor)
                # the egg doesn't break (add max # floors that we can check above the current floor)
                # add current floor (+1)
                print(m, e, dp)
                if dp[m][e] >= n:
                    return m
        return n

# Solution 2
# Time: O(k * log n), Space: O(k)
class Solution2(object):
    def superEggDrop(self, k, n):
        # define two dps, interchange each other
        dp_prev = [0] * (k + 1)
        dp_curr = [0] * (k + 1)
        m = 0
        while dp_prev[k] < n:
            m += 1
            for e in range(1, k+1):
                dp_curr[e] = dp_prev[e - 1] + dp_prev[e] + 1
            dp_prev, dp_curr = dp_curr, dp_prev

        return m


# Test case
solution = Solution2()

k = 3; n = 14
result = solution.superEggDrop(k, n)
print(result) # 4