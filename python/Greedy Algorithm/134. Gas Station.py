# 134. Gas Station
# https://leetcode.com/problems/gas-station/

# Date: Dec 23, 2023
# Difficulty: Medium

# Solution 1:
class Solution1(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # iterate through each starting point
        for start in range(len(gas)):
            fuel = 0

            # simulate traveling from the current start point
            for i in range(start, len(gas) + start):
                index = i % len(gas)
                can_travel = True

                if gas[index] + fuel < cost[index]:
                    can_travel = False
                    break
                else:
                    fuel += gas[index] - cost[index]

            if can_travel:
                return start

        return -1

# Solution 2
class Solution2(object):
    def canCompleteCircuit(self, gas, cost):
        # check if it is possible to complete the circuit
        if sum(gas) < sum(cost):
            return -1

        # given that the solution is unique
        start, fuel = 0, 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start


# Test case 1
solution = Solution1()
gas = [1,2,3,4,5]; cost = [3,4,5,1,2]
result = solution.canCompleteCircuit(gas, cost)
print(result) # 3

# Test case 2
solution = Solution2()
gas = [2,3,4]; cost = [3,4,3]
result = solution.canCompleteCircuit(gas, cost)
print(result) # -1