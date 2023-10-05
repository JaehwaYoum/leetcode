# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

# Date: Oct 5, 2023
# Difficulty: Medium

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # define expand function that returns the palindrome substring
        def expand(left, right):
            while left>=0 and right<=len(s) and s[left] == s[right-1]:
                left -=1
                right +=1
            return s[left+1:right-1]

        # exceptional cases (string shorter than 1 character, string itself is palindrom)
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # iterate through s to check for the maximum palindrome substring
        for i in range(len(s)):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
            # expand(i, i+1): palindrome with even number of characters
            # expand(i, i+2): palindrome with odd number of characters

        return result

# Test case
solution = Solution()

s = "babad"
result = solution.longestPalindrome(s)
print(result)