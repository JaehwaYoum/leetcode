# 1041. Robot Bounded In Circle
# https://leetcode.com/problems/robot-bounded-in-circle/

# Date: Jan 29, 2025
# Difficulty: Medium

# Solution
# Time: O(n), Space: O(1)
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """

        direction = (0, 1)  # Left: -> (-1, 0) -> (0, -1) -> (1, 0)
                            # Right: -> (1, 0) -> (0, -1) -> (-1, 0)
        start = [0, 0]  # initial position

        for i in instructions:
            if i == 'G':  
                start[0] += direction[0]
                start[1] += direction[1]
            elif i == 'L':  
                direction = (-direction[1], direction[0])
            elif i == 'R':  
                direction = (direction[1], -direction[0])

        return start == [0, 0] or direction != (0, 1)


# Test case
solution = Solution()

instructions = "GGLLGG"
result = solution.isRobotBounded(instructions)

print(result) # True
