# 316. Remove Duplicate Letters
# https://leetcode.com/problems/remove-duplicate-letters/

# Date: Nov 29, 2023
# Difficulty: Medium

# Solution 1: recursive
# Time: O(n^2 log n), Space: O(n^2)
import collections
class Solution1(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''

# Solution 2: stack
# Time: O(n), Space: O(n)
class Solution2(object):
    def removeDuplicateLetters(self, s):
        counter = collections.Counter(s)
        seen, stack = set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] >0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)

# Test case
solution = Solution1()

s = "cbacdcbc"
result = solution.removeDuplicateLetters(s)
print(result)