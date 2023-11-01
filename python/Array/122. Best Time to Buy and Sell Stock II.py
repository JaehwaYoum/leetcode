# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Date: Aug 19, 2023
# Difficulty: Medium

# Time: O(n), Space: O(1)
# Solution 1
class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0

        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])

        return profit

# Time: O(n), Space: O(1)
# Solution 2
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        check = 0
        buy = sell = 0
        profit = 0

        for i in range(len(prices)):
            if i == 0:
                buy = prices[0]
            elif prices[i] >= check:
                sell = prices[i]
            elif prices[i] < check:
                profit += max(sell - buy, 0)
                buy = prices[i]
                sell = 0
            check = prices[i]

        if check == sell:
            profit += max(sell - buy, 0)

        return profit


# Test case
solution = Solution1()

prices = [7,1,5,3,6,4]
result = solution.maxProfit(prices)
print(result)