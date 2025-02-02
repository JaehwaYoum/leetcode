# 1232. Check If It Is a Straight Line
# https://leetcode.com/problems/check-if-it-is-a-straight-line/

# Date: Jan 30, 2025
# Difficulty: Easy

# Solution
# Time: O(n log n), Space: O(1)
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        # slope = (y2 - y1) / (x2 - x1)

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            # x, y slope = (y - y1) / (x - x1)
            # if (y - y1) / (x - x1) != (y2 - y1) / (x2 - x1):
            if (y - y1) * (x2 - x1) != (y2 - y1) * (x - x1):
                return False
        return True


# Test case
solution = Solution()

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
result = solution.checkStraightLine(coordinates)

print(result) # True