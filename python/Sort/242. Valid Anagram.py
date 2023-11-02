# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

# Date: Aug 20, 2023
# Difficulty: Easy

import collections

# Solution 1: dictionary
# Time: O(n), Space: O(1)
class Solution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        dict1, dict2 = {}, {}

        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for j in t:
            if j in dict2:
                dict2[j] += 1
            else:
                dict2[j] = 1

        if dict1 == dict2:
            return True

        return False

# Solution 2: merge sort
# Time: O(n), Space: O(1)
class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        char_list = 'abcdefghijklmnopqrstuvwxyz'
        count_list = [0] * 26
        index = 0

        for i in s:
            index = char_list.index(i)
            count_list[index] += 1

        for j in t:
            index = char_list.index(j)
            count_list[index] -= 1

        return all(element == 0 for element in count_list)

# Solution 3: collections.Counter (similar to Solution 1)
# Time: O(n), Space: O(1)
class Solution3(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        coll1 = collections.Counter(s)
        coll2 = collections.Counter(t)

        return coll1 == coll2

# Test case
solution = Solution3()
s = "anagram"
t = "nagaram"
result = solution.isAnagram(s,t)
print(result) # True
