# 844. Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/ 

# Date: Jan 5, 2025
# Difficulty: Easy


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        stack_s, stack_t = [], []

        for char in stack_s:
            if stack_s and char == '#':
                stack_s.pop(char)
            elif char == '#':
                continue
            else:
                stack_s.append(char)
        for char in stack_t:
            if stack_t and char == '#':
                stack_t.pop(char)
            elif char == '#':
                continue
            else:
                stack_t.append(char)

        return stack_s == stack_t # order of items in lists are maintained 

# Test case
solution = Solution()

s = "a#c"; t = "b"
result = solution.backspaceCompare(s, t)
print(result) # False