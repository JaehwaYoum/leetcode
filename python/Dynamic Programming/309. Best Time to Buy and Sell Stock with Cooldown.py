# 309. Best Time to Buy and Sell Stock with Cooldown 
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

# Date: Aug 17, 2024
# Difficulty: Medium

# Solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <=1:
            return 0

        # dp[i][0] no stock on hold
        # dp[i][1] stock on hold
        dp = [[0, 0] for i in range(n + 1)]
        dp[1][1] = -prices[0]

        for i in range(2, n + 1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i-1])
        return max(dp[-1])


# Test case
solution = Solution()

prices = [1,2,3,0,2]
result = solution.maxProfit(prices)
print(result) 