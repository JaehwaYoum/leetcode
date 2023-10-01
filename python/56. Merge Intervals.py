# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/

# Date: Aug 22, 2023
# Difficulty: Medium

# Time: O(n*log(n)), Space: O(n)
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()
        merged_intervals = []

        for interval in intervals:
            if not merged_intervals or interval[0] > merged_intervals[-1][1]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = interval[1]

        return merged_intervals

# Test case
solution = Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]
result = solution.merge(intervals)
print(result)
