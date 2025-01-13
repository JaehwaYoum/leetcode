# 9. Palindrome Number
# https://leetcode.com/problems/reverse-integer/description/

# Date: Jan 13, 2025
# Difficulty: Easy

# Solution 1: String conversion
# Time: O(n), Space: O(n)
class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string_x = str(x)
        return string_x == string_x[::-1]


# Solution 2: Reference to 7. Reverse Integer
# Time: O(n), Space: O(1)
class Solution2(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        num, rev = x, 0
        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod

        return num == rev


# Test case
solution = Solution2()

x = -123
result = solution.reverse(x)
print(result) # False