# 344. Reverse String
# https://leetcode.com/problems/reverse-string/


# Date: Sep 29, 2023
# Difficulty: Easy

class Solution1(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        s.reverse()

class Solution2(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        s[:] = s[::-1]

# Test case
solution = Solution2()

s = ["h","e","l","l","o"]
solution.reverseString(s)
print(s)