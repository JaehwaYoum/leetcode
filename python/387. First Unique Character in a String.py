# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/

# Date: Sep 24, 2023
# Difficulty: Easy

# Time: O(n), Space: O(n)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        frequency = {}
        for c in s:
            frequency[c] = frequency.get(c, 0) + 1

        for i in range(len(s)):
            if frequency[s[i]] == 1:
                return i
        return -1

# Test case
solution = Solution()

s = "loveleetcode"
result = solution.firstUniqChar(s)
print(result) # 2