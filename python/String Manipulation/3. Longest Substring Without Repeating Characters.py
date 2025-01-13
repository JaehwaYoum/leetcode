# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Date: Nov 28, 2023
# Difficulty: Medium

# Solution 1: Dictionary {char: index}
# Time: O(n), Space: O(n)
import collections
class Solution1(object):
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

# Solution 2: Character set
# Time: O(n), Space: O(n)
class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        result = 0
        char_set = set()
        left = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            result = max(result, right - left + 1)

        return result


# Test case
solution = Solution2()

s = "abcabcbb"
result = solution.lengthOfLongestSubstring(s)
print(result) # 3
