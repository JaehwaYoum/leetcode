# 819. Most Common Word
# https://leetcode.com/problems/most-common-word/

# Date: Sep 29, 2023
# Difficulty: Easy

import re
import collections

# Time: O(m*log(m)), Space: O(m)
# m:the number of words in the paragraph
class Solution1(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        split = re.sub(r'[^\w]', ' ', paragraph).lower().split()
        words = [word for word in split if word not in banned]  
        word_cnt = collections.Counter(words)

        return word_cnt.most_common(1)[0][0]


# Test case
solution = Solution()

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
result = solution.mostCommonWord(paragraph, banned)
print(result)