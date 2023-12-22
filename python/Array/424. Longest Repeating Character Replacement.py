# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/

# Date: Dec 13, 2023
# Difficulty: Medium

# Solution 1: sliding window & counter
# Time: O(n), Space: O(1)
import collections
class Solution1(object):
    def characterReplacement(self, s, k):
        left = right = 0
        counts = collections.Counter()

        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            max_char_n = counts.most_common(1)[0][1] # frequency of the most frequent character

            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1

        return right - left

# Solution 2: calculate max length as it iterates through the string
# Time: O(n), Space: O(1)
class Solution2(object):
    def characterReplacement(self, s, k):
        left = 0
        seen = collections.defaultdict(int)
        max_length = 0

        for right in range(len(s)):
            seen[s[right]] += 1

            cnt = right - left + 1
            if cnt - max(seen.values()) <= k:
                max_length = max(max_length, cnt)

            else:
                seen[s[left]] -= 1
                if not seen[s[left]]:
                    seen.pop(s[left])
                left += 1

        return max_length

# Test case
solution = Solution2()
s = "AABABBA"
k = 1
result = solution.characterReplacement(s, k)
print(result) # 4