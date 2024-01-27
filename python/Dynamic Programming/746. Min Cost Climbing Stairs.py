# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/description/

# Date: Jan 27, 2024
# Difficulty: Easy

# Solution:
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # initialize the min_cost list
        min_cost = [0] * len(cost)

        # you can either start at index 0 or 1
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]

        # add up the minimum costs
        for i in range(2, len(cost)):
            min_cost[i] = cost[i] + min(min_cost[i - 1], min_cost[i - 2])

        # return the smaller of the last two elements
        return min(min_cost[-1], min_cost[-2])

# Test case
solution = Solution()

cost = [1,100,1,1,1,100,1,1,100,1]
result = solution.minCostClimbingStairs(cost)
print(result) # 6


