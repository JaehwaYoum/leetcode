# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Date: Nov 28, 2023
# Difficulty: Medium

# Solution 1
import collections
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic = collections.defaultdict(int)
        length = 0
        start = 0 

        for end, char in enumerate(s):
            if char in dic and dic[char] >= start:
                start = dic[char] + 1
            
            dic[char] = end
            length = max(length, end-start+1)

        return length
    
# Test case
solution = Solution()

s = "abcabcbb"
result = solution.lengthOfLongestSubstring(s)
print(result) # 3
