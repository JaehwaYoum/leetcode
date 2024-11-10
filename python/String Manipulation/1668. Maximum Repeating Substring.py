# 1668. Maximum Repeating Substring
# https://leetcode.com/problems/maximum-repeating-substring/description/

# Date: Nov 10, 2024
# Difficulty: Easy

# Solution
# Time: O(n * m), Space: O(m)
class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        n, m = len(sequence), len(word)
        if n < m:
            return 0

        result = 0
        i = 0
        while i < n - m + 1:
            curr_result = 0

            while sequence[i:i+m] == word:
                curr_result += 1 
                i += m

            i = i - curr_result * m + 1
            result = max(result, curr_result)

        return result



# Test case
solution = Solution()
sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaaba"
result = solution.maxRepeating(sequence, word)
print(result) # 5