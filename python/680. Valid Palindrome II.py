# 680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome/

# Date: Jul 15, 2023
# Difficulty: Easy

# Solution 1
# Time: O(n), Space: O(n)
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def is_palindrome(s):
            return s == s[::-1]

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                substring_1 = s[left:right]
                substring_2 = s[left + 1:right + 1]
                return is_palindrome(substring_1) or is_palindrome(substring_2)
            else:
                left += 1
                right -= 1
        return True


# Test case
solution = Solution()

s = "abc"
result = solution.validPalindrome(s)
print(result)