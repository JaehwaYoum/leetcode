# 2289. Steps to Make Array Non-decreasing
# https://leetcode.com/problems/steps-to-make-array-non-decreasing/description/

# Date: Feb 2, 2025
# Difficulty: Medium

# Solution
# Time: O(n), Space: O(n)
class Solution(object):
    def totalSteps(self, nums):
        result = 0
        stack = [[nums[0], 0]]  # stores number and step count

        for num in nums[1:]:
            step_count = 0
            while stack and stack[-1][0] <= num:
                step_count = max(step_count, stack[-1][1])
                stack.pop()
            
            if stack:
                step_count += 1
            else:
                step_count = 0

            result = max(result, step_count)
            stack.append([num, step_count])

        return result


# Test case
solution = Solution()

nums = [5,3,4,4,7,3,6,11,8,5,11]
result = solution.totalSteps(n)
print(result) # 3