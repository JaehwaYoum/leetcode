# 518. Coin Change II
# https://leetcode.com/problems/coin-change-ii/

# Date: Sep 24, 2023
# Difficulty: Medium

# Time: O(n * amount), Space: O(amount)
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [1] + [0] * amount
        for i in coins:
            for j in range(1, amount + 1):
               if j >= i:
                   dp[j] += dp[j - i]
        return dp[amount]

# Test case
solution = Solution()

coins = [1,2,5]
amount = 6
result = solution.change(amount, coins)
print(result) # 5