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
solution = Solution()

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
result = solution.reorderLogFiles(logs)
print(result)