# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

# Date: Jul 15, 2023
# Difficulty: Easy

# Solution 1
# Time: O(n), Space: O(n)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_strip = [c.lower() for c in s if c.isalnum()]

        left = 0
        right = len(s_strip) - 1

        while left < right:
            if s_strip[left] != s_strip[right]:
                return False
            left += 1
            right -= 1

        return True

# Test case
solution = Solution()

s = "A man, a plan, a canal: Panama"
result = solution.isPalindrome(s)
print(result)
