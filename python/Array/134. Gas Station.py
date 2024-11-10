# 134. Gas Station
# https://leetcode.com/problems/gas-station

# Date: Nov 9, 2024
# Difficulty: Medium

# Time: O(n), Space: O(1)
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1

        curr_gas, start_idx = 0, 0
        for i in range(len(gas)):
            curr_gas += gas[i] - cost[i]
            if curr_gas < 0:
                curr_gas = 0
                start_idx = i + 1  

        return start_idx


# Test case
solution = Solution()
gas = [1,2,3,4,5]; cost = [3,4,5,1,2]
result = solution.canCompleteCircuit(gas, cost)
print(result)