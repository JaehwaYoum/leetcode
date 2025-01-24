# 459. Repeated Substring Pattern
# https://leetcode.com/problems/repeated-substring-pattern/

# Date: Jan 18, 2025
# Difficulty: Easy

# Solution 1
# Time: O(n^2), Space: O(1)
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)

        for i in range(1, n//2 + 1):
            if n % i == 0 and s[:i] * (n//i) == s:
                return True

        return False


# Solution 2: One-liner
# Time: O(n), Space: O(n)
class Solution2(object):
    def repeatedSubstringPattern(self, s):
        return s in (s + s)[1:-1]


# Test case
solution = Solution2()

s = "aba"
result = solution.repeatedSubstringPattern(s)
print(result) # false
