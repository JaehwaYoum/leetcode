# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

# Date: Jan 13, 2025
# Difficulty: Easy

# Time: O(n), Space: O(1)
# Solution 1
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        length = 0
        i = len(s) - 1

        while i >= 0 and s[i] == " ":
            i -= 1 
        
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length


# Time: O(n), Space: O(n)
# Solution 2
class Solution2(object):
    def lengthOfLastWord(self, s): 
        words = s.strip().split(" ")

        if not words:
            return 0

        return len(words[-1])

# Test case
solution = Solution1()

s = "   fly me   to   the moon  "
result = solution.lengthOfLastWord(s)
print(result) # 4