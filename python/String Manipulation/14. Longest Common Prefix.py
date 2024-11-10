# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/

# Date: Nov 9, 2024
# Difficulty: Easy

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        first_str = strs[0]

        for i in range(len(first_str)):
            char_to_check = first_str[i]
            for string in strs[1:]:
                # If the character doesn't match or we reach the end of a string, return the prefix found so far
                if i >= len(string) or string[i] != char_to_check:
                    return first_str[:i]
        return first_str



# Test case
solution = Solution()

strs = ["flower","flow","flight"]
result = solution.longestCommonPrefix(strs)
print(result)