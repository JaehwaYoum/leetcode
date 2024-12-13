# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Date: Jul 17, 2023
# Difficulty: Easy

# Solution 1
# Time: O(n), Space: O(1)
class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) < 2:
            return 0

        profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            elif price - min_price > profit:
                profit = price - min_price

        return profit

# Solution 2
# Time: O(n), Space: O(1)
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) < 2:
            return 0

        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            profit = prices[right] - prices[left]

            if prices[left] < prices[right]:
                max_profit = max(max_profit, profit)
            else:
                left = right

            right += 1

        return max_profit


# Solution 3
# Time: O(n), Space: O(1)
class Solution3(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price-min_price)

        return profit

# Test case
solution = Solution3()

prices = [7,1,5,3,6,4]
result = solution.maxProfit(prices)
print(result) # 5