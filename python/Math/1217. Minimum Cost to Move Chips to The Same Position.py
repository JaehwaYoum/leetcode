# 1217. Minimum Cost to Move Chips to The Same Position
# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

# Date: Mar 25, 2024
# Difficulty: Easy

# Solution 1
class Solution1(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """

        even = odd = 0
        for i in range(len(position)):
            if position[i] % 2 == 0:
                even += 1
            else:
                odd += 1

        return min(even, odd)

# Solution 2: faster runtime
class Solution2(object):
    def minCostToMoveChips(self, position):
        even = 0
        for i in position:
            if(i % 2 == 0):
                even += 1
        return min(even, len(position) - even)


# Test case
solution = Solution2()

position = [1,2,3]
result = solution.minCostToMoveChips(position)

print(result) # 1
