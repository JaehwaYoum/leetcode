# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/

# Date: Aug 25, 2024
# Difficulty: Medium

# Solution

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) <= 1:
            return 0

        result = 0
        left, right = 0, len(height)-1

        while left < right:
            area = min(height[left], height[right]) * (right-left)
            result = max(area, result)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result


# Test case
solution = Solution()

height = [1,8,6,2,5,4,8,3,7]
result = solution.maxArea(height)
print(result)


