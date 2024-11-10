# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

# Date: Nov 9, 2024
# Difficulty: Easy

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        len_haystack = len(haystack)
        len_needle = len(needle)

        if len_needle == 0 or len_haystack < len_needle:
            return -1

        i, j = 0, 0

        while i < len_haystack:
            if haystack[i] != needle[j]:
                # start again
                i = i - j 
                j = 0                
            else:
                # go until we finish the needle 
                j += 1
                if j == len_needle:
                    return i - j + 1
            i += 1

        # reached the end of the haystack, without a match 
        return -1 




# Test case
solution = Solution()

haystack = "leetcode"
needle = "leeto"
result = solution.strStr(haystack, needle)
print(result)