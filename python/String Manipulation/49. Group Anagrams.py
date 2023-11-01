# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

# Date: Oct 5, 2023
# Difficulty: Medium

# Solution 1
# Time: O(n * k * log(k)), Space: O(n * k)
# k :the length of the longest word, n: number of words in the list

import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # create a dictionary
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return anagrams.values()

# Test case
solution = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
result = solution.groupAnagrams(strs)
print(result)