    # 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

# Date: Dec 18, 2023
# Difficulty: Medium

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stack = [] # stores the index of the higher temperatures

        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                result[last] = i - last
            stack.append(i)

        return result

# Test case
solution = Solution()
temperatures = [73,74,75,71,69,72,76,73]
result = solution.dailyTemperatures(temperatures)
print(result) # [1, 1, 4, 2, 1, 1, 0, 0]