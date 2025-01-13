# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/

# Date: Jan 13, 2025
# Difficulty: Easy

import collections
# Time: O(n), Space: O(1)
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """ 
        d1 = collections.Counter(ransomNote)
        d2 = collections.Counter(magazine)

        return all(key in d2 and d1[key] <= d2[key] for key in d1)
        #return d1 & d2 == d1 


# Test case
solution = Solution()

ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
result = solution.canConstruct(ransomNote, magazine):
print(result) # true