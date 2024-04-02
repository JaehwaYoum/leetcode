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

        # Initialize a dp array with size 'amount + 1'.
        # The first element is 1 because there's 1 way to make up amount 0 (i.e., no coins).
        dp = [1] + [0] * amount

        for coin in coins:
            # calculate the number of ways to make each amount from 1 and up to amount
            for current_amount in range(1, amount + 1):

               if current_amount >= coin:
                   dp[current_amount] += dp[current_amount - coin]
        return dp[amount]

# Test case
solution = Solution()

coins = [1,2,5]
amount = 6
result = solution.change(amount, coins)
print(result) # 5