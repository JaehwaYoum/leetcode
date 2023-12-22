# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

# Date: Nov 29, 2023
# Difficulty: Easy

# Solution 1
# Time: O(n), Space: O(n)
class Solution1(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        start = []
        for i in s:

            if i in "({[":
                start.append(i)
            if i in ")]}" and start==[]:
                return False
            if i ==")" :
                if start[-1] == "(":
                    start.pop()
                else:
                    return False
            if i =="]" :
                if start[-1] == "[":
                    start.pop()
                else:
                    return False
            if i =="}" :
                if start[-1] == "{":
                    start.pop()
                else:
                    return False

        return not bool(start)

# Solution 2: used stack, improved readability
# Time: O(n), Space: O(n)
class Solution2(object):
    def isValid(self, s):
        stack = []
        table = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False

        return len(stack) == 0


# Test case
solution = Solution2()

s = "()[]{}"
result = solution.isValid(s)
print(result)