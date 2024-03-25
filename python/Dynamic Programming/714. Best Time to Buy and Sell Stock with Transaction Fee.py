# 714. Best Time to Buy and Sell Stock with Transaction Fee
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

# Date: March 25, 2024
# Difficulty: Medium

# Solution: Dynamic Programming
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        # dp[i][0]: max profit without stock, dp[i][1]: max profit with stock
        dp = [[0,0] for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            # on day i without a stock, decide between selling today vs not holding a stock
            dp[i][0] = max(prices[i] + dp[i+1][1] - fee, dp[i+1][0])

            # on day i with a stock, decide between buying today vs not selling a stock
            dp[i][1] = max(-prices[i] + dp[i+1][0], dp[i+1][1])

        # return the max profit on day 0 with the optionality to buy the stock
        return dp[0][1]
        


# Test case
solution = Solution()

prices = [1,3,2,8,4,9]; fee = 2
result = solution.maxProfit(prices, fee)

print(result) # 8
