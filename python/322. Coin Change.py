# 322. Coin Change
# https://leetcode.com/problems/coin-change/submissions/

# Date: Sep 24, 2023
# Difficulty: Medium

# Time: O(n * amount), Space: O(amount)
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf') for i in range(amount)]
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]


# Test case
solution = Solution()

coins = [1,2,5]
amount = 6
result = solution.coinChange(coins, amount)
print(result) # 2