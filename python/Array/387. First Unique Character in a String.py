# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/

# Date: Jul 6, 2024
# Difficulty: Easy

import collections
# Solution
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        frequency = collections.defaultdict(int)

        for char in s:
            frequency[char] += 1

        for i in range(len(s)):
            if frequency[s[i]] == 1:
                return i

        return -1


# Test case
solution = Solution()
s = "loveleetcode"
result = solution.firstUniqChar(s)
print(result) # 2
        