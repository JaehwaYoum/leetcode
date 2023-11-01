# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

# Date: Oct 5, 2023
# Difficulty: Hard

# Solution 1: two pointers
# Time: O(n), Space: O(1)
class Solution1(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        volume = 0
        left, right = 0, len(height)-1
        max_left, max_right = height[left], height[right]

        while left < right:
            if max_left <= max_right:
                volume += max_left- height[left]
                left += 1
            else:
                volume += max_right - height[right]
                right -= 1

            max_left, max_right = max(max_left, height[left]), max(max_right, height[right])

        return volume

# Solution 2: stack
# Time: O(n), Space: O(n)
class Solution2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        stack = [] # adds up the area horizontally
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]: # higher bar appeared
                top = stack.pop() # pop the previous index

                if not stack: # if the bars were adjacent, no volume
                    break

                width = i - stack[-1] - 1
                length = min(height[i], height[stack[-1]]) - height[top]
                volume += width * length

            stack.append(i) # append the index to the stack

        return volume

# Test case
solution = Solution2()

height = [0,1,0,2,1,0,1,3,2,1,2,1]
result = solution.trap(height)
print(result) # 6