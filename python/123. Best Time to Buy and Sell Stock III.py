# 123. Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# Date: Sep 09, 2023
# Difficulty: Difficult


# Time: O(n), Space: O(1)
# Solution 1
class Solution1(object):
    def maxProfit(self, p):
        if len(p) == 0:
            return 0

        k = 2
        states = [0] + [-float('inf') for i in range(2 * k)]
        states[1] = -p[0]

        for i in range(1, len(p)):
            for j in range(k):
                states[2 * j + 1] = max(states[2 * j + 1], states[2 * j] - p[i])
                states[2 * j + 2] = max(states[2 * j + 2], states[2 * j + 1] + p[i])
            print(states)

        return max(0, states[-1])

# Time: O(n), Space: O(1)
# Solution 2
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        right = n - 1
        left = n - 2
        best_left = -1
        max_profit_1, max_profit_2 = 0, 0

        while left >= 0:
            profit = prices[right] - prices[left]
            if prices[right] > prices[left]:
                max_profit_1 = max(max_profit_1, profit)
                if max_profit_1 == profit:
                    best_left = left
            else:
                right = left
            left -= 1

        right = best_left
        left = best_left - 1

        while left >= 0:
            profit2 = prices[right] - prices[left]
            if prices[right] > prices[left]:
                max_profit_2 = max(max_profit_2, profit2)
            else:
                right = left
            left -= 1

        right = n - 1
        left = right - 2

        while left >= best_left:
            profit3 = prices[right] - prices[left]
            if prices[right] > prices[left]:
                max_profit_2 = max(max_profit_2, profit3)
            else:
                right = left
            left -= 1

        return max_profit_1 + max_profit_2


# Test case
solution = Solution1()

prices = [3,3,5,0,0,3,1,4]
result = solution.maxProfit(prices)
print(result)
