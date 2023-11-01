# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/

# Date: Aug 28, 2023
# Difficulty: Medium

# Time: O(2^n), binary tree
# Space: O(n)

# Solution 1
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []

        def parenthesis(left, right, s):

            if left:
                parenthesis(left - 1, right, s + '(')

            if right > left:
                parenthesis(left, right - 1, s + ')')

            if not right:
                result.append(s)

        parenthesis(n, n, '')

        return result

# Test case
solution = Solution()

n = 3
result = solution.generateParenthesis(n)
print(result)
# ['((()))', '(()())', '(())()', '()(())', '()()()']