# 389. Find the Difference
# https://leetcode.com/problems/find-the-difference/

# Date: Jan 16, 2025
# Difficulty: Easy

import collections

# Solution 1: collections counter dict
# Time: O(n), Space: O(1)
class Solution1(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d_s, d_t = collections.Counter(s), collections.Counter(t)
        return [key for key in d_t if d_t[key] != d_s[key]][0]


# Solution 2: direct count 
 # Time: O(n^2), Space: O(1)
class Solution2(object):
    def findTheDifference(self, s, t):
        for i in t:
            if s.count(i) != t.count(i):
                return i

# Solution 3: ASCII code
# Time: O(n), Space: O(1)
class Solution3(object):
    def findTheDifference(self, s, t):
        sum_s = sum(ord(i) for i in s)
        sum_t = sum(ord(j) for j in t)
        return chr(sum_t - sum_s)


# Test case
solution = Solution2()
s = "abcd"; t = "abcde"
result = solution.findTheDifference(s, t)
print(result) # "e"
