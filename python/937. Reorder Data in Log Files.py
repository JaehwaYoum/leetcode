# 937. Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/

# Date: Sep 29, 2023
# Difficulty: Medium

# Time: O(n), Space: O(n)
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        letters = []
        digits = []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

# Test case
solution = Solution2()

s = ["h","e","l","l","o"]
solution.reverseString(s)
print(s)